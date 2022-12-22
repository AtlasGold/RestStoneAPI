from httpx import get, patch, post
from test.utils import BASE_URL, ClearDatabase, NonexistentMessage, RandomText, MakeVotes


def test_valid_vote():
    """
    Insert a message via post 
    and then add a vote
    """
    ClearDatabase()
    post(BASE_URL, json={"text": RandomText()})
    request = patch(BASE_URL + "/0")
    assert request.status_code == 200
    ClearDatabase()


def test_vote_nonexistent_message():
    """
    Test to realize nem vote an message that does
    not exist in the database
    """
    request = patch(BASE_URL + f"{NonexistentMessage()}")
    assert request.status_code == 404


def test_make_vote_with_invalid_message_id():
    """
    tries to poll a non-existent 
    message by passing an invalid id
    """
    request = patch(BASE_URL + "/P4R4N@ID")
    assert request.status_code == 404

def test_vote_with_null_value():
    """
    Try to perform a vote where no id or
    value is passed in the url
    """
    request = patch(BASE_URL + "/")
    assert request.status_code == 404


def test_perform_multiple_votes_differents_messages():
    """  
    Test generates five messages and performs five 
    votes on all of them. You are expected to return 
    the five messages with your five votes
    """
    ClearDatabase()
    for i in range(5):
        post(BASE_URL, json={"text" : RandomText()})
        MakeVotes(5, i)
        i += 1
    for y in range(5):
        request = get(BASE_URL + f"/{y}")
        assert request.status_code == 200 and request.json()['votes'] == 5

def test_perform_multiple_votes_same_message():
    """  
    Generates a message and then adds a vote
    each time and checks if the votes were
    generated one after the other
    """

    ClearDatabase()
    post(BASE_URL, json={"text" : "Back In Black"})
    
    patch(BASE_URL + "/0")
    first_request = get(BASE_URL + "/0")
    assert first_request.status_code == 200 and first_request.json() == {"id": 0,"text": "Back In Black","votes": 1}
    
    patch(BASE_URL + "/0")
    second_request = get(BASE_URL + "/0")
    assert second_request.status_code == 200 and second_request.json() == {"id": 0,"text": "Back In Black","votes": 2}

