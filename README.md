[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/DESIFpxz)

# Tarot Spread

A web application for tarot card readings, allowing users to draw spreads, view card meanings, and track their history.

## Features

- **Draw Spreads**: Choose between 3, 5, or 10-card spreads.
- **Card Meanings**: Upright and reversed meanings for all 78 cards.
- **History Tracking**: View past spreads and their details.
- **Interactive UI**: Simple and intuitive browser-based interface.

## Getting Started

### Prerequisites
- Docker
- Docker Compose

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd cs-project-2025-matveidetonator
   ```

2. Build and run the application:
   ```bash
   docker compose up --build -d
   ```

3. Open the application in your browser:
   [http://localhost:5000](http://localhost:5000)

## API Documentation

Interactive API documentation is available at:
[http://localhost:5000/api/docs](http://localhost:5000/api/docs)

### Endpoints

#### Spreads
- `GET /api/tarot/spread/three` - Retrieve a 3-card spread.
- `GET /api/tarot/spread/five` - Retrieve a 5-card spread.
- `GET /api/tarot/spread/ten` - Retrieve a 10-card spread.

#### Cards
- `GET /api/tarot/cards` - Retrieve all cards in the deck.
- `GET /api/tarot/cards/<id>` - Retrieve a specific card by ID.

#### History
- `GET /api/tarot/history` - Retrieve the history of spreads.

## Project Structure

```
cs-project-2025-matveidetonator/
├── backend/
│   ├── app.py           # Flask server
│   ├── models.py        # Database models
│   ├── seed_cards.py    # Deck initialization
│   ├── test_api.py      # Unit and integration tests
│   └── static/
│       └── swagger.json # API documentation
├── client/
│   └── index.html       # Web interface
└── docker-compose.yml   # Docker configuration
```

## Tech Stack

- **Backend**: Python 3.11, Flask, Flask-SQLAlchemy
- **Database**: PostgreSQL
- **Frontend**: HTML, CSS, JavaScript
- **Deployment**: Docker, Docker Compose

## Running Tests

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Run tests using pytest:
   ```bash
   pytest
   ```

## CI/CD

- **CI**: GitHub Actions for automated testing and builds.
- **CD**: Deployment using Docker Compose.

## Success Criteria

- Backend responds correctly to all API requests.
- Client verifies server responses.
- All tests pass successfully.
- API documentation is accessible via Swagger UI.
- Application is production-ready and deployable.