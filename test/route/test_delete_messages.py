from httpx import post, delete
from test.utils import BASE_URL, RandomText, ClearDatabase, NonexistentMessage


def test_valid_deletion():
    """
    Test a valid selection that
    shouldn't return anything
    """
    ClearDatabase()
    post(BASE_URL, json={"text": RandomText()})
    request = delete(BASE_URL + "/0")
    assert request.status_code == 204


def test_delete_nonexistent_message():
    """
    Test to delete an image that does
    not exist in the database
    """
    request = delete(BASE_URL + f"{NonexistentMessage()}")
    assert request.status_code == 404


def test_null_value():
    """
    Delete test with URL missing values
    """
    request = delete(BASE_URL + "/")
    assert request.status_code == 404


def test_delete_with_invalid_value():
    """
    Test for selection with invalid values
    that do not match ID
    """
    request = delete(BASE_URL + "/P4R4N@ID")
    assert request.status_code == 404
