# UserBot-LiteS

> 🎛️ Lightweight Telegram UserBot — full-feature starter (Telethon)
>
> Repo ini adalah starter kit UserBot berbasis Telethon (akun user), berisi fitur broadcast/share, payment receipt, admin tools, media tools, automation, dan tools lainnya.

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![Telethon](https://img.shields.io/badge/Telethon-1.x-orange)](https://docs.telethon.dev/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

---

## 🔥 Logo & Bahasa Pemrograman
Logo (opsional): letakkan file logo di `assets/logo.png` dan tambahkan di README dengan markdown:

```markdown
![UserBot Logo](assets/logo.png)

Bahasa & teknologi yang digunakan / didukung:

JavaScript (JS) — untuk script helper atau integrasi frontend

PHP — contoh integrasi webhook/payment server-side (opsional)

HTML & CSS — halaman info / dashboard sederhana (opsional)

Python — core userbot (Telethon + modules)

React.js — alternatif UI dashboard (opsional)


> NOTE: Repo inti ini ditulis 100% di Python (Telethon). Bahasa lain disebut sebagai opsi/pendukung bila kamu ingin membuat web dashboard, API, atau integrasi pembayaran.




---

📦 Fitur Utama

.menu / .help — daftar fitur & command

Broadcast & Share (kirim ke semua kontak / grup)

Payment system: .payment, .done, .paylog, .setpay — buat struk pembayaran otomatis

AI tools: .ask, .translate (bila API disetel)

Admin tools: ban, kick, promote, demote, purge

Media tools: konversi gambar ke sticker, download media

Security: antilink, antiflood

Logging aktivitas, penyimpanan ke SQLite



---

⚙️ Cara Install & Run (Termux / Linux)

1. Clone repo:



git clone https://github.com/AlwaysPrimess/UserBot-LiteS.git
cd UserBot-LiteS

2. (Opsional) Buat venv:



python -m venv venv
source venv/bin/activate

3. Install dependensi:



pip install -r requirements.txt

4. Isi config.py:



api_id, api_hash dari https://my.telegram.org

owner_id = Telegram user id (angka)

CMD_PREFIX (default .)

payment_methods dan ai_api_key jika perlu


5. Jalankan:



python main.py

Masukkan nomor telepon dan kode OTP saat diminta.


---

🔐 Keamanan & Saran

Jangan jalankan userbot dengan akun utama yang digunakan untuk hal penting. Gunakan akun testing bila perlu.

Set owner_id agar hanya kamu yang dapat menjalankan command admin / shell / eval.

Backup data/userbot.db secara berkala jika menyimpan pembayaran/riwayat.



---

🧩 Struktur Project (singkat)

.
├─ main.py
├─ config.py
├─ requirements.txt
├─ modules/
│  ├─ basic.py
│  ├─ payment.py
│  ├─ broadcast.py
│  └─ ...
├─ utils/
│  ├─ db.py
│  └─ text_template.py
└─ data/
   └─ userbot.db


---

🔁 Kontribusi

Pull requests welcome. Jika ingin tambahkan fitur (dashboard React/Node, gateway pembayaran, webhook), buat issue/PR.


---

📜 Lisensi

MIT — silakan atur LICENSE sesuai kebutuhan.


---

Kontak

Untuk bantuan setup cepat atau fitur custom: @viosf_12 (ganti dengan kontakmu)
