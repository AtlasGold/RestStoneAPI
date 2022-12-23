from httpx import get, post, put
from test.utils import BASE_URL, RandomText, ClearDatabase, NonexistentMessage


def test_update_noexistent_message():
    """
    Test done to test update message
    that does not exist
    """
    request = put(BASE_URL + f"/{NonexistentMessage()}", json={"text": "Pink Floyd"})
    assert request.status_code == 404 and request.json() == {
        "message": "Message doesn't exists!"
    }


def test_update_existent_message():
    """
    Generate a message and then
    update the value to a valid text
    """
    ClearDatabase()
    post(BASE_URL, json={"text": "Dark Side of The Sun"})
    request = put(BASE_URL + "/0", json={"text": "The Dark Side of the Moon"})
    assert request.status_code == 200 and request.json() == {
        "text": "The Dark Side of the Moon"
    }
    ClearDatabase()


def test_update_message_with_the_same_value():
    """
    Try to update the value of a message
    with the same previously registered
    value that should not be allowed
    """
    ClearDatabase()
    post(BASE_URL, json={"text": "I Was Made for Lovin' You by KISS"})
    request = put(BASE_URL + "/0", json={"text": "I Was Made for Lovin' You by KISS"})
    assert request.status_code == 409 and request.json() == {
        "message": "The message is the same!"
    }
    ClearDatabase()


def test_update_message_sucessfully():
    """
    Test to perform a successful update
    """
    ClearDatabase()
    post(BASE_URL, json={"text": "Hire me Jader"})
    request = put(BASE_URL + "/0", json={"text": "I will make it worth"})
    assert request.status_code == 200 and request.json() == {
        "text": "I will make it worth"
    }
    ClearDatabase()


def test_update_with_invalid_url():
    """
    Test an update with the malformed URL
    """
    request = put(BASE_URL + "/1NV4LID_URI", json={"text": RandomText()})
    assert request.status_code == 404


def test_more_fields_than_necessary():
    """
    Tests an update where more fields
    than it should are passed in the JSON body
    """
    ClearDatabase()
    post(BASE_URL, json={"text": RandomText()})
    request = put(BASE_URL + "/0", json={"id": 0, "text": "Black Babbath", "votes": 0})
    assert request.status_code == 200 and request.json() == {"text": "Black Babbath"}
    ClearDatabase()


def test_not_string_value():
    """
    Attempts to update a message with
    a text value that is not of type: STRING
    """
    ClearDatabase()
    post(BASE_URL, json={"text": RandomText()})
    request = put(BASE_URL + "/0", json={"text": []})
    assert request.status_code == 422 and request.json() == [
        {"loc": ["text"], "msg": "str type expected", "type": "type_error.str"}
    ]
