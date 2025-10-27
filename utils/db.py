import sqlite3
from datetime import datetime
from config import db_path
import os

class DB:
    def __init__(self, path=db_path):
        self.path = path
        self._ensure()

    def _ensure(self):
        if not os.path.exists(os.path.dirname(self.path)):
            os.makedirs(os.path.dirname(self.path), exist_ok=True)
        conn = sqlite3.connect(self.path)
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS payments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ts INTEGER,
                nominal TEXT,
                jenis TEXT,
                info TEXT,
                by_user TEXT
            )
        ''')
        c.execute('''
            CREATE TABLE IF NOT EXISTS settings (
                key TEXT PRIMARY KEY,
                value TEXT
            )
        ''')
        conn.commit()
        conn.close()

    def insert_payment(self, record):
        conn = sqlite3.connect(self.path)
        c = conn.cursor()
        c.execute('INSERT INTO payments (ts, nominal, jenis, info, by_user) VALUES (?,?,?,?,?)',
                  (record['timestamp'], record['nominal'], record['jenis'], record['info'], record['by']))
        conn.commit()
        conn.close()

    def get_payments(self, limit=50):
        conn = sqlite3.connect(self.path)
        c = conn.cursor()
        c.execute('SELECT ts, nominal, jenis, info, by_user FROM payments ORDER BY ts DESC LIMIT ?', (limit,))
        rows = c.fetchall()
        conn.close()
        out = []
        for r in rows:
            out.append({
                'timestamp': r[0],
                'nominal': r[1],
                'jenis': r[2],
                'info': r[3],
                'by': r[4],
                'ts_str': datetime.fromtimestamp(r[0]).strftime('%Y-%m-%d %H:%M:%S')
            })
        return out

    def set_setting(self, key, value):
        conn = sqlite3.connect(self.path)
        c = conn.cursor()
        c.execute('REPLACE INTO settings (key, value) VALUES (?,?)', (key, value))
        conn.commit()
        conn.close()

    def get_setting(self, key):
        conn = sqlite3.connect(self.path)
        c = conn.cursor()
        c.execute('SELECT value FROM settings WHERE key=?', (key,))
        row = c.fetchone()
        conn.close()
        return row[0] if row else None
