from httpx import get, post
from test.utils import BASE_URL, RandomText, DatabaseSize, ClearDatabase, MakeVotes


def test_connetion_get_messages():
    """
    Send a request to test the
    connection to the API routes
    """
    request = get(BASE_URL)
    assert request.status_code == 200, "Status code was different than 200"


def test_getting_no_messages():
    """
    Test a request that should returns no value
    because the database should have been
    created a short time ago
    """
    request = get(BASE_URL)
    assert (
        request.json() == {"Messages": [], "count": 0} and request.status_code == 200
    ), "Database was not empty. Have you tested the API before? Try run tests again!"


def test_getting_one_message():
    """
    Creates a mocked insertion via API in an
    empty database and tests if the introduced
    values are the same ones to be requested by GET
    """
    ClearDatabase()

    post(BASE_URL, json={"text": "foo"})

    request = get(BASE_URL)
    assert (
        request.json()
        == {
            "Messages": [{"id": 0, "text": "foo", "votes": 0}],
            "count": 1,
        }
        and request.status_code == 200
    )

    ClearDatabase()


def test_find_message_by_id():
    """
    Insert two messages and try to receive
    only the message with the specified id on get
    """
    ClearDatabase()

    post(BASE_URL, json={"text": "message with id zero"})
    post(BASE_URL, json={"text": "message with id one"})

    request = get(BASE_URL + f"/{1}")
    assert (
        request.json() == {"id": 1, "text": "message with id one", "votes": 0}
        and request.status_code == 200
    )

    ClearDatabase()


def test_try_find_invalid_id():

    request = get(BASE_URL + "/apple")
    assert request.status_code == 404


def test_filter_random_messages_by_votes():
    """
    Test that inserts two messages and adds five
    votes to one. It is necessary to return
    only messages with five votes or more. If
    the number of votes does not exist, return
    an error of not found
    """
    ClearDatabase()
    post(BASE_URL, json={"text": "message that will receive votes"})
    post(BASE_URL, json={"text": "message with zero votes"})
    MakeVotes(5, 0)
    request = get(BASE_URL + f"/random/{5}")

    assert request.json() == {
        "id": 0,
        "text": "message that will receive votes",
        "votes": 5,
    }
    ClearDatabase()


def test_try_find_message_with_invalid_votes():
    """
    Attempting to find a random message with a
    minimum number of votes too large to exist.
    """
    request = get(BASE_URL + f"/random/{999999999}")

    assert request.status_code == 404 and request.json() == {
        "message": "There are NO Messages with these number of Votes!"
    }


def test_count_messages_are_correct():
    """
    Enters five text messages and checks
    that the count actually shows five
    """
    for i in range(5):
        post(BASE_URL, json={"text": RandomText()})
        i += 1
    request = get(BASE_URL)
    assert request.json()["count"] == 5

    ClearDatabase()
