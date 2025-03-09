def test_get_order_status(test_client):
    payload = {
        "query": "Where is my order?"
        }
    response = test_client.post(
        "/api/support-agent",
        json=payload
     )
    assert response.status_code == 200
    response_json = response.json()

    assert response_json["response"] 
    assert response_json["query"] == payload["query"]

def test_create_order_status_with_user_data(test_client):
    payload = {
        "query": "I want to place a new order",
        "username": "Faiz",
        "phone": "+9188499883"
        }
    response = test_client.post(
        "/api/support-agent",
        json=payload
     )
    assert response.status_code == 200

    response_json = response.json()
    assert response_json["response"] 
    assert response_json["query"] == payload["query"]


def handled_un_recognized_query(test_client):
    payload = {
        "query": "What is my Name?"
        }
    response = test_client.post(
        "/api/support-agent",
        json=payload
     )
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["response"] == "Sorry, I don't understand your request."