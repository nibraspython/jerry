import re
from os import environ

help_message = []

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

SESSION = environ.get('SESSION', 'jerrybot')
API_ID = int(environ.get('API_ID', '23648338'))
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
SECONDDB_URI = environ.get('SECONDDB_URI', None)
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "oggytg")
API_HASH = environ.get('API_HASH', '9b23c1dda0eaf6c48758d4c1e6ae9fe0')
PICS = (environ.get('PICS' ,'https://graph.org/file/01ddfcb1e8203879a63d7.jpg https://graph.org/file/d69995d9846fd4ad632b8.jpg')).split()
BOT_TOKEN = environ.get('BOT_TOKEN', '7191755037:AAETjjIHi0dcWBpvaR5LZk9fz3mO_x5IvbM')
MSG_ALRT = environ.get('MSG_ALRT', 'You Fool!? 😩')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001938307351'))
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
PORT = environ.get("PORT", "8080")

