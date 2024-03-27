import re
from os import environ

SESSION = environ.get('SESSION', 'small_bot')
API_ID = int(environ.get('API_ID', '23381624'))
API_HASH = environ.get('API_HASH', '02e5d155e1abcdb51673733ecc088a29')
BOT_TOKEN = environ.get('BOT_TOKEN', '7019442694:AAEPow32KsK9UMSx1btpKkE_TwGBqBExqQE')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001668201351'))
PORT = environ.get("PORT", "8080")
