import json
from tests import client

# This file tests the API with end-to-end test using a mock client.

def test_post_request_example_data(client):
    """Test function to test app.py. 
    The test uses a test client that simulates the API's 
    functioning without opening it to any port.

    """
    json_data =(
        {
        "cart_value": 790,
        "delivery_distance": 2235,
        "number_of_items": 4,
        "time": "2021-10-12T13:00:00Z"
    }
    )
    # Sending data to test client
    response = client.post(
        "/",
        headers={"Content-Type": "application/json"}, 
        data=json.dumps(json_data)
        )
    # Convert response to a json format
    json_response = json.loads(response.text)
    # Check if the response is correct
    assert json_response["delivery_fee"] == 710


def test_post_request_friday_rush(client):
    """Test function to test app.py. 
    The test uses a test client that simulates the API's 
    functioning without opening it to any port.

    """
    json_data =(
        {
        "cart_value": 790,
        "delivery_distance": 2235,
        "number_of_items": 4,
        "time": "2023-01-27T16:00:00Z"
    }
    )
    # Sending data to test client
    response = client.post(
        "/",
        headers={"Content-Type": "application/json"}, 
        data=json.dumps(json_data)
        )
    # Convert response to a json format
    json_response = json.loads(response.text)
    # Check if the response is correct
    assert json_response["delivery_fee"] == 852

def test_unallowed_request(client):
    """Testing API with a GET request to make sure it does not allow it.

    """
    response = client.get(
        "/",
        )
    # Check if the response is correct
    assert response.status_code == 405

