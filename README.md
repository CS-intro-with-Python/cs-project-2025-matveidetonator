[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/DESIFpxz)

# Tarot Spread

A web application for tarot card readings — draw spreads, read card meanings (upright and reversed), and browse past readings.

---

## 🚀 Quick start

### Run with Docker (recommended)

1. Build and run services:

```bash
docker compose up --build -d
```

2. Open:
- App: http://localhost:5000
- API docs (Swagger UI): http://localhost:5000/api/docs

### Run locally (without Docker)

1. Create and activate a virtual environment (Python 3.11 recommended):

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r backend/requirements.txt
```

3. (Optional) Set the database URL if not using the Docker PostgreSQL service:

```bash
export DATABASE_URL='postgresql://user:pass@localhost:5432/tarot'
```

4. Start the backend:

```bash
python backend/app.py
```

> The backend will attempt to create the database schema and seed the deck on startup.

---

## 🔧 Environment

- DATABASE_URL — SQLAlchemy-style connection string (default used in Docker: `postgresql://tarot:tarot@db:5432/tarot`).
- The backend listens on port `5000` by default.

---

## 📡 API Endpoints (examples)

- Draw spreads:
  - GET /api/tarot/spread/three  → 3-card spread
  - GET /api/tarot/spread/five   → 5-card spread
  - GET /api/tarot/spread/ten    → 10-card spread

- Cards:
  - GET /api/tarot/cards         → list all cards (supports `?suit=`)
  - GET /api/tarot/cards/<id>    → get card by ID

- History:
  - GET /api/tarot/history?limit=10

Quick curl examples:

```bash
curl http://localhost:5000/api/tarot/spread/three
curl http://localhost:5000/api/tarot/cards | jq
curl 'http://localhost:5000/api/tarot/history?limit=5'
```

---

## 🧪 Tests

Run tests locally from the `backend/` folder:

```bash
cd backend
pytest
```

Or inside the running backend container:

```bash
docker compose exec backend pytest
```

---

## 📁 Project structure

```
cs-project-2025-matveidetonator/
├── backend/               # Flask API, models, tests and seeding script
│   ├── app.py
│   ├── models.py
│   ├── seed_cards.py
│   ├── requirements.txt
│   └── tests/
├── client/                # Static client (index.html + assets)
│   ├── index.html
│   └── web_server.py?     # optional helper to serve assets locally
├── docker-compose.yml
└── README.md
```

---

## 📚 Tech stack

- Backend: Python 3.11, Flask, Flask-SQLAlchemy
- Database: PostgreSQL
- Frontend: HTML / CSS / vanilla JS
- Deployment: Docker, Docker Compose

---

## ✅ Notes & Changelog

- 2026-01-16 — README updated: added local development instructions, environment variables, curl examples, and test commands.

---

## Contributing

Contributions and fixes are welcome via pull requests. Keep changes small, add tests where appropriate, and update the README or docs when adding features.

---

If you want, I can also add a short `Makefile` or `dev` scripts to simplify common tasks (run, test, lint). ✨
