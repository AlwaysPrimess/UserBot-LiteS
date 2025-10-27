from telethon import events
from config import CMD_PREFIX
from modules import payment  # to ensure referenced modules exist

def register(client):
    @client.on(events.NewMessage(pattern=fr'^{CMD_PREFIX}menu$', outgoing=True))
    async def menu(evt):
        menu_text = f"""
📜 UserBot Menu

Utility:
{CMD_PREFIX}help — bantuan singkat
{CMD_PREFIX}ping — test koneksi
{CMD_PREFIX}alive — status userbot
{CMD_PREFIX}id — info id pengguna/chat

Payment Menu:
{CMD_PREFIX}payment — daftar metode pembayaran
{CMD_PREFIX}done <nominal>, <jenis>, <info> — catat pembayaran
{CMD_PREFIX}paylog — riwayat pembayaran
{CMD_PREFIX}setpay <nama>, <no> — ubah data payment

Broadcast & Share:
{CMD_PREFIX}share — reply pesan -> kirim ke semua grup
{CMD_PREFIX}broadcast — reply pesan -> kirim ke semua kontak

AI & Tools:
{CMD_PREFIX}ask <teks> — tanya AI
{CMD_PREFIX}translate <teks> — terjemah teks
{CMD_PREFIX}tts <teks> — teks->suara
{CMD_PREFIX}stt — voice->text (reply audio)

System:
{CMD_PREFIX}sysinfo — info VPS
{CMD_PREFIX}shell <cmd> — jalankan perintah shell
{CMD_PREFIX}eval <code> — eksekusi python
{CMD_PREFIX}update — update userbot

Admin Tools:
{CMD_PREFIX}ban <reply/uid> — ban user
{CMD_PREFIX}kick <reply/uid> — kick user
{CMD_PREFIX}promote <reply/uid> — promote
{CMD_PREFIX}demote <reply/uid> — demote

Media Tools:
{CMD_PREFIX}sticker — reply foto -> sticker
{CMD_PREFIX}download — reply media -> download

Security:
{CMD_PREFIX}antilink on/off
{CMD_PREFIX}antiflood on/off

Channel Me : 
t.me/viosaja13
t.me/viosaja12

Room Public :
t.me/publicvios
t.me/watch_crash

Use commands by sending them as your own message (outgoing)."""
        await evt.reply(menu_text)
