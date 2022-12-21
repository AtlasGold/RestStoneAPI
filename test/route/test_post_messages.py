from httpx import get, post
from test.utils import BASE_URL, RandomText, DatabaseSize, ClearDatabase, MakeVotes


def test_add_message():
    ClearDatabase()
    """
    Send a simple message
    """
    request = post(BASE_URL, json={"text": "Master Of Puppets"})
    assert request.status_code == 200 and request.json() == {
        "id": 0,
        "text": "Master Of Puppets",
        "votes": 0,
    }


def test_insert_repeated_message():
    """
    Try to enter the same message twice
    """
    ClearDatabase()
    first_request = post(BASE_URL, json={"text": "Waiting Silence by Angra"})
    assert first_request.status_code == 200 and first_request.json() == {
        "id": 0,
        "text": "Waiting Silence by Angra",
        "votes": 0,
    }
    second_request = post(BASE_URL, json={"text": "Waiting Silence by Angra"})
    assert second_request.status_code == 402 and second_request.json() == {
        "message": "Message alredy exists!"
    }
    ClearDatabase()


def test_autoincrement_id_messages():
    """
    Insert your texts and check if the id
    auto-incrementer will return the fifth
    value as five (it starts to iterate from 0)
    """
    ClearDatabase()
    for i in range(6):
        post(BASE_URL, json={"text": RandomText()})
        i += 1
    request = get(BASE_URL + "/5")
    assert request.json()["id"] == 5 and request.status_code == 200
    ClearDatabase()


def test_insert_not_string_value():
    """
    Tests the insertion of invalid values
    """
    request = post(BASE_URL, json={"text": []})
    assert request.status_code == 422


def test_insert_empty_value():
    """
    Empty value insertion test
    """
    request = post(BASE_URL, json={"text": ""})
    assert (
        request.json() == {"id": 0, "text": "", "votes": 0}
        and request.status_code == 200
    )

    request = post(BASE_URL, json={"text": ""})
    assert request.json() == {"message": "Message alredy exists!"}
    ClearDatabase()


def test_put_more_than_expect():
    """  
    Test to directly insert the ID and vote
    values ​​that should be ignored by the 
    API and use the default values
    """
    ClearDatabase()
    request = post(BASE_URL, json={"id": 101, "text": "Lagwagon", "votes": 99})
    assert request.json() == {"id": 0, "text": "Lagwagon", "votes": 0}

