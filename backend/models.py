"""Database models for Tarot application."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Card(db.Model):
    """Tarot card model."""
    __tablename__ = 'cards'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    suit = db.Column(db.Text, nullable=True)  # NULL for Major Arcana
    rank = db.Column(db.Text, nullable=True)  # NULL for Major Arcana
    meaning_upright = db.Column(db.Text, nullable=False)
    meaning_reversed = db.Column(db.Text, nullable=False)
    image_path = db.Column(db.Text, nullable=False)
    
    def to_dict(self):
        """Convert card to dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'suit': self.suit,
            'rank': self.rank,
            'meaning_upright': self.meaning_upright,
            'meaning_reversed': self.meaning_reversed,
            'image_path': self.image_path
        }


class Spread(db.Model):
    """Tarot spread (reading) model."""
    __tablename__ = 'spreads'
    
    id = db.Column(db.Integer, primary_key=True)
    spread_type = db.Column(db.String(50), nullable=False)
    cards = db.Column(db.JSON, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    
    def to_dict(self):
        """Convert spread to dictionary."""
        return {
            'id': self.id,
            'type': self.spread_type,
            'cards': self.cards,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }
