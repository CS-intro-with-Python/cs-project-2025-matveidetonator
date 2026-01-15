"""Tarot API Flask Application."""
import os
import random
import time

from flask import Flask, jsonify, send_from_directory, request
import sqlalchemy.exc
from flask_swagger_ui import get_swaggerui_blueprint

from models import db, Card, Spread
from seed_cards import seed_database

# Flask setup
app = Flask(__name__, static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL', 
    'postgresql://tarot:tarot@db:5432/tarot'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db.init_app(app)

# Enable CORS for all origins (public)
from flask_cors import CORS
CORS(app)


# Swagger setup
SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI
API_URL = '/static/swagger.json'  # Path to the Swagger JSON file
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Tarot API"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)


# API Routes
@app.route('/api/tarot/spread/<string:kind>')
def get_spread(kind):
    """Draw tarot cards for a reading."""
    spread_counts = {'three': 3, 'five': 5, 'ten': 10}
    if kind not in spread_counts:
        app.logger.warning(f"Invalid spread type requested: {kind}")
        return jsonify({'error': 'Invalid spread type.'}), 400
    
    count = spread_counts[kind]
    
    all_cards = Card.query.all()
    if not all_cards:
        app.logger.error("No cards found in database!")
        return jsonify({'error': 'No cards in database.'}), 500
    
    drawn_cards = random.sample(all_cards, count)
    cards_data = []
    for card in drawn_cards:
        card_dict = card.to_dict()
        card_dict['orientation'] = random.choice(['upright', 'reversed'])
        cards_data.append(card_dict)
    
    spread = Spread(spread_type=kind, cards=cards_data)
    db.session.add(spread)
    db.session.commit()
    
    app.logger.info(f"Drew {count} card(s): {[c['name'] for c in cards_data]}")
    return jsonify(spread.to_dict())


@app.route('/api/tarot/history')
def get_history():
    """Get history of all tarot readings."""
    limit = request.args.get('limit', 10, type=int)
    spreads = Spread.query.order_by(Spread.created_at.desc()).limit(limit).all()
    total = Spread.query.count()
    
    app.logger.info(f"Retrieved {len(spreads)} spreads from history")
    return jsonify({'spreads': [s.to_dict() for s in spreads], 'total': total})


@app.route('/api/tarot/cards')
def get_cards():
    """Get all tarot cards in the deck."""
    suit = request.args.get('suit')
    
    if suit:
        cards = Card.query.filter_by(suit=suit).all()
    else:
        cards = Card.query.all()
    
    app.logger.info(f"Retrieved {len(cards)} cards")
    return jsonify({'cards': [c.to_dict() for c in cards], 'total': len(cards)})


@app.route('/api/tarot/cards/<int:card_id>')
def get_card(card_id):
    """Get a specific card by ID."""
    card = Card.query.get(card_id)
    if not card:
        app.logger.warning(f"Card not found: {card_id}")
        return jsonify({'error': 'Card not found'}), 404
    
    app.logger.info(f"Retrieved card: {card.name}")
    return jsonify(card.to_dict())


# Wait for DB and initialize
def wait_for_db():
    for attempt in range(30):
        try:
            with app.app_context():
                db.create_all()
                # Seed database with cards
                seed_database(db, Card)
                app.logger.info("Database initialized")
            return
        except sqlalchemy.exc.OperationalError:
            time.sleep(2)
    raise RuntimeError("Database not available")


# Serve client UI
@app.route('/')
def index():
    return send_from_directory('/client', 'index.html')


# Initialize database on startup
wait_for_db()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)