from datetime import datetime

def format_receipt(record: dict) -> str:
    ts = datetime.fromtimestamp(record['timestamp']).strftime('%Y-%m-%d %H:%M:%S')
    lines = [
        '✅ PAYMENT RECEIPT',
        '────────────────────────',
        f"Nama: {record.get('by')}",
        f"Jenis: {record.get('jenis')}",
        f"Nominal: {record.get('nominal')}",
        f"Info: {record.get('info')}",
        f"Tanggal: {ts}",
        'Status: SUKSES ✅',
        '────────────────────────',
        'Terima kasih telah melakukan pembayaran'
    ]
    return '\n'.join(lines)
