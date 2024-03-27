import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

SESSION = environ.get('SESSION', 'jerrybot')
API_ID = int(environ.get('API_ID', '23648338'))
API_HASH = environ.get('API_HASH', '9b23c1dda0eaf6c48758d4c1e6ae9fe0')
PICS = (environ.get('PICS' ,'https://graph.org/file/01ddfcb1e8203879a63d7.jpg https://graph.org/file/d69995d9846fd4ad632b8.jpg')).split()
BOT_TOKEN = environ.get('BOT_TOKEN', '6926402548:AAECdcA1FcyxGfDWlBZbtAFYLY_DF19NI8g')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001771073047'))
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
PORT = environ.get("PORT", "8080")
