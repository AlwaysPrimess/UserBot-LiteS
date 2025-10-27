from telethon import events
from config import CMD_PREFIX, owner_id
import re

STATE = {
    'antilink': False,
    'antiflood': False
}

link_re = re.compile(r'http[s]?://')

def register(client):
    @client.on(events.NewMessage(pattern=fr'^{CMD_PREFIX}antilink\s+(on|off)$', outgoing=True))
    async def antilink_toggle(evt):
        if evt.sender_id != owner_id:
            return await evt.reply('Forbidden')
        val = evt.pattern_match.group(1)
        STATE['antilink'] = (val == 'on')
        await evt.reply(f'Antilink set to {STATE["antilink"]}')

    @client.on(events.NewMessage(incoming=True))
    async def antilink_check(evt):
        if not STATE['antilink']:
            return
        if link_re.search(evt.raw_text or ''):
            try:
                await evt.delete()
            except Exception:
                pass

    @client.on(events.NewMessage(pattern=fr'^{CMD_PREFIX}antiflood\s+(on|off)$', outgoing=True))
    async def antiflood_toggle(evt):
        if evt.sender_id != owner_id:
            return await evt.reply('Forbidden')
        val = evt.pattern_match.group(1)
        STATE['antiflood'] = (val == 'on')
        await evt.reply(f'Antiflood set to {STATE["antiflood"]}')
