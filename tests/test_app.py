import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_signup_and_unregister():
    # Setup: create a temporary activity
    from src.app import activities
    temp_activity = "TempTestActivity"
    activities[temp_activity] = {
        "description": "Temporary activity for testing",
        "schedule": "Test schedule",
        "max_participants": 5,
        "participants": []
    }
    email = "testuser@example.com"
    # Sign up
    signup_resp = client.post(f"/activities/{temp_activity}/signup?email={email}")
    assert signup_resp.status_code == 200
    # Unregister
    unregister_resp = client.post(f"/activities/{temp_activity}/unregister?participant={email}")
    assert unregister_resp.status_code == 200
    # Cleanup
    del activities[temp_activity]
