from telethon import events
from config import CMD_PREFIX, ai_api_key
import aiohttp

AI_API = "https://api.openai.com/v1/chat/completions"

async def chatgpt(prompt, key):
    headers = {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}
    json = {"model": "gpt-3.5-turbo", "messages": [{"role": "user", "content": prompt}]}
    async with aiohttp.ClientSession() as s:
        async with s.post(AI_API, headers=headers, json=json) as r:
            if r.status != 200:
                return f"Error: {r.status}"
            data = await r.json()
            return data['choices'][0]['message']['content']

def register(client):
    @client.on(events.NewMessage(pattern=fr'^{CMD_PREFIX}ask\s+(.+)$', outgoing=True))
    async def ask(evt):
        if not ai_api_key:
            return await evt.reply('AI API key not set in config.py')
        q = evt.pattern_match.group(1)
        await evt.reply('💭 Sedang berpikir...')
        result = await chatgpt(q, ai_api_key)
        await evt.reply(result)

    @client.on(events.NewMessage(pattern=fr'^{CMD_PREFIX}translate\s+(.+)$', outgoing=True))
    async def translate(evt):
        text = evt.pattern_match.group(1)
        api = f"https://api.mymemory.translated.net/get?q={text}&langpair=id|en"
        async with aiohttp.ClientSession() as s:
            async with s.get(api) as r:
                data = await r.json()
                translated = data['responseData']['translatedText']
        await evt.reply(f"Terjemahan: {translated}")
