import re

def parse_done_text(text):
    parts = [p.strip() for p in text.split(',')]
    return parts
