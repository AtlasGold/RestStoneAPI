import random
import string
from httpx import delete, get, patch


BASE_URL = "http://127.0.0.1:1234/messages"


def DatabaseSize():
    request = get(BASE_URL)
    response = request.json()["count"]
    return response


def ClearDatabase():
    for i in range(DatabaseSize()):
        delete(BASE_URL + f"/{i}")


def MakeVotes(votes_number: int, message_id: int):
    for i in range(votes_number):
        patch(BASE_URL + f"/{message_id}", json={"id": message_id})
        i += 1


def RandomChar():
    return "".join(random.choices(string.ascii_letters, k=1))


def RandomText():
    return "".join(random.choices(string.ascii_letters, k=12))
