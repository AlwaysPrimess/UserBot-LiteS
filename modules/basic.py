from telethon import events
from config import CMD_PREFIX

def register(client):
    @client.on(events.NewMessage(pattern=fr'^{CMD_PREFIX}ping$', outgoing=True))
    async def ping(evt):
        await evt.reply('Pong!')

    @client.on(events.NewMessage(pattern=fr'^{CMD_PREFIX}alive$', outgoing=True))
    async def alive(evt):
        me = await client.get_me()
        await evt.reply(f"Userbot aktif sebagai {me.first_name} (@{getattr(me, 'username', '')})")

    @client.on(events.NewMessage(pattern=fr'^{CMD_PREFIX}id(?:\s+(.+))?$', outgoing=True))
    async def get_id(evt):
        # jika reply, tunjukkan info message target
        if evt.is_reply:
            msg = await evt.get_reply_message()
            await evt.reply(f'Chat id: {msg.chat_id}\nFrom user id: {msg.sender_id}')
        else:
            await evt.reply(f'Your chat id: {evt.chat_id}\nYour id: {evt.sender_id}')

    @client.on(events.NewMessage(pattern=fr'^{CMD_PREFIX}help$', outgoing=True))
    async def help_cmd(evt):
        text = (
            'Commands:\n'
            f'{CMD_PREFIX}menu - show full menu\n'
            f'{CMD_PREFIX}ping - test\n'
            f'{CMD_PREFIX}alive - status\n'
            f'{CMD_PREFIX}id - show id\n'
            f'{CMD_PREFIX}share - reply text -> share ke semua grup\n'
            f'{CMD_PREFIX}broadcast - reply text -> send to all contacts\n'
            f'{CMD_PREFIX}payment - show payment methods\n'
            f'{CMD_PREFIX}done - mark payment\n'
        )
        await evt.reply(text)
