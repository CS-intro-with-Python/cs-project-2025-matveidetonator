import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from models import Card, Spread
import pytest
import datetime

# Unit test for Card.to_dict()
def test_card_to_dict():
    card = Card(
        id=1,
        name="The Fool",
        suit=None,
        rank=None,
        meaning_upright="New beginnings, optimism",
        meaning_reversed="Recklessness, risk",
        image_path="cards/the_fool.jpg"
    )
    result = card.to_dict()
    assert result["id"] == 1
    assert result["name"] == "The Fool"
    assert result["meaning_upright"] == "New beginnings, optimism"
    assert result["meaning_reversed"] == "Recklessness, risk"
    assert result["image_path"] == "cards/the_fool.jpg"
    assert result["suit"] is None
    assert result["rank"] is None

# Unit test for Spread.to_dict()
def test_spread_to_dict():
    now = datetime.datetime.now()
    spread = Spread(
        id=2,
        spread_type="three",
        cards=[{"name": "The Fool"}, {"name": "The Magician"}, {"name": "The High Priestess"}],
        created_at=now
    )
    result = spread.to_dict()
    assert result["id"] == 2
    assert result["type"] == "three"
    assert isinstance(result["cards"], list)
    assert result["cards"][0]["name"] == "The Fool"
    assert result["created_at"].startswith(str(now.year))
