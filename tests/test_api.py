import pytest
from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_summarize_endpoint():
    test_text = " ".join(["This is a test sentence."] * 50)
    
    response = client.post("/summarize", json={
        "text": test_text,
        "ratio": 0.2,
        "algorithm": "abstractive"
    })
    
    assert response.status_code == 200
    data = response.json()
    assert "summary" in data
    assert len(data["summary"]) < len(test_text)
    assert 0 <= data["readability_score"] <= 100

def test_invalid_algorithm():
    response = client.post("/summarize", json={
        "text": "Valid text",
        "algorithm": "invalid_method"
    })
    
    assert response.status_code == 400
    assert "Invalid algorithm" in response.json()["detail"]