# main.py — bootstrap Telethon dan load module
import asyncio
import logging
import os
from telethon import TelegramClient
from config import api_id, api_hash, session_name

# create data dir
if not os.path.exists('data'):
    os.makedirs('data', exist_ok=True)

# logging
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')
logger = logging.getLogger('userbot')

# Telethon client
client = TelegramClient(session_name, api_id, api_hash)

# load modules (import paths must exist)
from modules import basic, menu, payment, share, broadcast, ai_tools, system, autoreply, admin_tools, media_tools, security, logger as mod_logger

async def main():
    await client.start()
    me = await client.get_me()
    logger.info(f"Started userbot as {me.first_name} (@{getattr(me, 'username', '')}) id={me.id}")

    # register modules
    for mod in [basic, menu, payment, share, broadcast, ai_tools, system, autoreply, admin_tools, media_tools, security, mod_logger]:
        try:
            mod.register(client)
            logger.info(f"Module loaded: {mod.__name__}")
        except Exception as e:
            logger.exception(f"Failed loading module {mod.__name__}: {e}")

    print("Userbot running. Tekan CTRL+C untuk berhenti.")
    await client.run_until_disconnected()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Stopping userbot...')
