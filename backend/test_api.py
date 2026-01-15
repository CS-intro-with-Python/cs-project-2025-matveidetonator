import pytest
import requests

BASE_URL = "http://localhost:5000/api/tarot/spread/"

@pytest.mark.parametrize("kind,count", [
    ("five", 5),
    ("three", 3)
])
def test_tarot_spread(kind, count):
    resp = requests.get(BASE_URL + kind)
    assert resp.status_code == 200
    data = resp.json()
    assert data["type"] == kind
    assert isinstance(data["cards"], list)
    assert len(data["cards"]) == count
    for card in data["cards"]:
        assert isinstance(card, dict)
        assert "name" in card
