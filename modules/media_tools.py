from telethon import events
from config import CMD_PREFIX
from PIL import Image
import io

def register(client):
    @client.on(events.NewMessage(pattern=fr'^{CMD_PREFIX}sticker$', outgoing=True))
    async def to_sticker(evt):
        if not evt.is_reply:
            return await evt.reply('Reply to an image to make sticker.')
        msg = await evt.get_reply_message()
        if not msg.media:
            return await evt.reply('No media found in replied message.')
        file = await client.download_media(msg.media)
        try:
            im = Image.open(file).convert('RGBA')
            im.thumbnail((512, 512))
            bio = io.BytesIO()
            bio.name = 'sticker.png'
            im.save(bio, 'PNG')
            bio.seek(0)
            await client.send_file(evt.chat_id, bio, force_document=False)
        except Exception as e:
            await evt.reply(f'Error: {e}')

    @client.on(events.NewMessage(pattern=fr'^{CMD_PREFIX}download$', outgoing=True))
    async def download(evt):
        if not evt.is_reply:
            return await evt.reply('Reply to media to download.')
        msg = await evt.get_reply_message()
        if not msg.media:
            return await evt.reply('No media found.')
        path = await client.download_media(msg.media, file='downloads/')
        await evt.reply(f'Downloaded to {path}')
