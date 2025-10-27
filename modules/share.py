from telethon import events
from config import CMD_PREFIX, owner_id, broadcast_delay
import asyncio

def is_group_entity(entity):
    # simple check: has title attribute and not user
    return getattr(entity, 'title', None) is not None

def register(client):
    @client.on(events.NewMessage(pattern=fr'^{CMD_PREFIX}share$', outgoing=True))
    async def share_all_groups(evt):
        if evt.sender_id != owner_id:
            return await evt.reply('Forbidden')
        if not evt.is_reply:
            return await evt.reply('Reply ke pesan yang ingin di-share ke semua grup')
        msg = await evt.get_reply_message()
        await evt.reply('Memulai share ke semua grup...')
        count = 0
        async for dialog in client.iter_dialogs():
            if is_group_entity(dialog.entity):
                try:
                    if msg.media:
                        await client.send_file(dialog.id, msg.media, caption=msg.text or '')
                    else:
                        await client.send_message(dialog.id, msg.text or '')
                    count += 1
                    await asyncio.sleep(broadcast_delay)
                except Exception:
                    continue
        await evt.reply(f'Done. Shared to {count} groups')
