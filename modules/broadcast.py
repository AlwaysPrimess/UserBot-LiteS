from telethon import events
from config import CMD_PREFIX, owner_id, broadcast_delay
import asyncio

def register(client):
    @client.on(events.NewMessage(pattern=fr'^{CMD_PREFIX}broadcast$', outgoing=True))
    async def broadcast_all(evt):
        if evt.sender_id != owner_id:
            return await evt.reply('Forbidden')
        if not evt.is_reply:
            return await evt.reply('Reply ke pesan yang ingin di-broadcast ke semua kontak/chat')
        msg = await evt.get_reply_message()
        await evt.reply('Memulai broadcast ke semua chat...')
        count = 0
        async for dialog in client.iter_dialogs():
            # kirim hanya ke private chats (users)
            if dialog.is_user:
                try:
                    if msg.media:
                        await client.send_file(dialog.id, msg.media, caption=msg.text or '')
                    else:
                        await client.send_message(dialog.id, msg.text or '')
                    count += 1
                    await asyncio.sleep(broadcast_delay)
                except Exception:
                    continue
        await evt.reply(f'Done. Broadcast sent to {count} contacts')
