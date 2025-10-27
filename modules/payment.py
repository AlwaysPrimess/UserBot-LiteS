from telethon import events
from config import CMD_PREFIX, owner_id, payment_methods
from utils.db import DB
from utils.text_template import format_receipt
import time

db = DB()

def register(client):
    @client.on(events.NewMessage(pattern=fr'^{CMD_PREFIX}payment$', outgoing=True))
    async def show_payment(evt):
        lines = ['Available payment methods:']
        for k, v in payment_methods.items():
            lines.append(f'- {k}: {v}')
        await evt.reply('\n'.join(lines))

    @client.on(events.NewMessage(pattern=fr'^{CMD_PREFIX}done\s+(.+)$', outgoing=True))
    async def mark_done(evt):
        if evt.sender_id != owner_id:
            return await evt.reply('Forbidden: only owner can mark payments.')
        text = evt.pattern_match.group(1).strip()
        parts = [p.strip() for p in text.split(',')]
        if len(parts) < 2:
            return await evt.reply('Format salah. Contoh: .done 25000, OVO, 08123456')
        nominal = parts[0]
        jenis = parts[1]
        info = parts[2] if len(parts) >= 3 else ''
        timestamp = int(time.time())
        rec = {
            'timestamp': timestamp,
            'nominal': nominal,
            'jenis': jenis,
            'info': info,
            'by': (await client.get_me()).username
        }
        db.insert_payment(rec)
        receipt = format_receipt(rec)
        await evt.reply(receipt)

    @client.on(events.NewMessage(pattern=fr'^{CMD_PREFIX}paylog$', outgoing=True))
    async def paylog(evt):
        rows = db.get_payments(limit=20)
        if not rows:
            await evt.reply('No payments logged.')
            return
        text_lines = ['Recent payments:']
        for r in rows:
            text_lines.append(f"- {r['nominal']} {r['jenis']} ({r['info']}) @ {r['ts_str']}")
        await evt.reply('\n'.join(text_lines))

    @client.on(events.NewMessage(pattern=fr'^{CMD_PREFIX}setpay\s+(.+)$', outgoing=True))
    async def setpay(evt):
        if evt.sender_id != owner_id:
            return await evt.reply('Forbidden')
        text = evt.pattern_match.group(1)
        parts = [p.strip() for p in text.split(',', 1)]
        if len(parts) != 2:
            return await evt.reply('Format salah. Contoh: .setpay OVO, 081234567')
        name, val = parts
        db.set_setting(f'pay_{name}', val)
        payment_methods[name] = val
        await evt.reply(f'Set {name} -> {val}')
