from telethon import events
from config import owner_id

AUTO_KEYWORDS = {
    'halo': 'Halo juga! Ada yang bisa dibantu?',
    'harga': 'Cek metode pembayaran dengan .payment ya!',
    'beli': 'Untuk pembelian silakan lakukan pembayaran lalu kirim .done'
}

def register(client):
    @client.on(events.NewMessage(incoming=True))
    async def auto_reply(evt):
        if evt.sender_id == owner_id:
            return
        text = (evt.raw_text or '').lower()
        for key, reply in AUTO_KEYWORDS.items():
            if key in text:
                await evt.reply(reply)
                break
