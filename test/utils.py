import random
import string

BASE_URL = 'http://127.0.0.1:1234/messages'
def RandomChar():
    return(''.join(random.choices(string.ascii_letters, k=1)))
def RandomText():
    return(''.join(random.choices(string.ascii_letters, k=12)))