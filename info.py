import re
from os import environ

SESSION = environ.get('SESSION', 'jerrybot')
API_ID = int(environ.get('API_ID', '23648338'))
API_HASH = environ.get('API_HASH', '9b23c1dda0eaf6c48758d4c1e6ae9fe0')
BOT_TOKEN = environ.get('BOT_TOKEN', '6926402548:AAECdcA1FcyxGfDWlBZbtAFYLY_DF19NI8g')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001771073047')
PORT = environ.get("PORT", "8080")
