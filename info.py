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
API_ID = int(environ.get('API_ID', '27761739'))
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
SECONDDB_URI = environ.get('SECONDDB_URI', None)
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://oggytgbot:oggytgbot@cluster0.bzdravq.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "oggytg")
API_HASH = environ.get('API_HASH', '68a5e625d16fc3759cddda0264f2110e')
PICS = (environ.get('PICS' ,'https://graph.org/file/01ddfcb1e8203879a63d7.jpg https://graph.org/file/d69995d9846fd4ad632b8.jpg')).split()
BOT_TOKEN = environ.get('BOT_TOKEN', '7582317858:AAEN3wjYk-1UBKXbQfMb2PpRn8_E3zrk1ik')
MSG_ALRT = environ.get('MSG_ALRT', 'You Fool!? 😩')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002328276546'))
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
PORT = environ.get("PORT", "8080")

