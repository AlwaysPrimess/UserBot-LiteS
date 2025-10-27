from telethon import events
from config import CMD_PREFIX, owner_id
import os, platform, psutil
import subprocess

def register(client):
    @client.on(events.NewMessage(pattern=fr'^{CMD_PREFIX}sysinfo$', outgoing=True))
    async def sysinfo(evt):
        cpu = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent
        try:
            uptime = subprocess.check_output(['uptime', '-p']).decode().strip()
        except Exception:
            uptime = 'unknown'
        text = f"""
💻 System Info
OS: {platform.system()} {platform.release()}
CPU: {cpu}%
RAM: {ram}%
Disk: {disk}%
Uptime: {uptime}
        """
        await evt.reply(text)

    @client.on(events.NewMessage(pattern=fr'^{CMD_PREFIX}shell\s+(.+)$', outgoing=True))
    async def shell(evt):
        if evt.sender_id != owner_id:
            return await evt.reply('Forbidden')
        cmd = evt.pattern_match.group(1)
        try:
            res = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, timeout=15).decode()
        except Exception as e:
            res = str(e)
        if len(res) > 1900:
            res = res[:1900] + "\n\n...[truncated]"
        await evt.reply(f"```\n{res}\n```", parse_mode='markdown')

    @client.on(events.NewMessage(pattern=fr'^{CMD_PREFIX}eval\s+(.+)$', outgoing=True))
    async def _eval(evt):
        if evt.sender_id != owner_id:
            return await evt.reply('Forbidden')
        code = evt.pattern_match.group(1)
        # very simple eval - for quick use, not production safe
        try:
            result = eval(code, {'client': client})
        except Exception as e:
            result = repr(e)
        await evt.reply(str(result))
