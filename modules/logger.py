from telethon import events
from config import log_path, CMD_PREFIX

def register(client):
    @client.on(events.NewMessage(outgoing=True))
    async def log_outgoing(evt):
        if evt.text and evt.text.startswith(CMD_PREFIX):
            with open(log_path, 'a', encoding='utf-8') as f:
                f.write(f'[OUT] {evt.date} {evt.sender_id}: {evt.text}\n')

    @client.on(events.NewMessage(incoming=True))
    async def log_incoming(evt):
        with open(log_path, 'a', encoding='utf-8') as f:
            f.write(f'[IN] {evt.date} {evt.sender_id}: {evt.raw_text}\n')
