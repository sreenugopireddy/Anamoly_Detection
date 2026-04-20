# Financial Transaction Anomaly Detection System

Real-time ML system that scores financial transactions, classifies risk levels, and logs alerts — built with FastAPI, Isolation Forest, and SQLite.

[![Python](https://img.shields.io/badge/Python-3.10+-blue)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green)](https://fastapi.tiangolo.com)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

---

## What It Does

Accepts raw transaction data via REST API, runs it through a feature engineering pipeline, scores it using an unsupervised ML model, classifies it as LOW / MEDIUM / HIGH risk, and persists high-risk alerts to a database — all in under 100ms per request.

---

## System Architecture

```
POST /score_transaction
         │
         ▼
┌─────────────────────┐
│  Feature Engineering │  ← amount, country, velocity, time features
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│  Isolation Forest    │  ← unsupervised anomaly scoring
│  Anomaly Scorer      │
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│  Risk Classifier     │  ← LOW / MEDIUM / HIGH thresholds
└─────────┬───────────┘
          │
     ┌────┴────┐
     ▼         ▼
  API        Alert Engine
Response   (HIGH only → SQLite)
     │
     ▼
Dashboard (GET /)
```

---

## Results

| Metric | Value |
|---|---|
| Dataset size | 50,000+ transactions |
| Model | Isolation Forest (unsupervised) |
| Risk levels | LOW / MEDIUM / HIGH |
| API response time | < 100ms per request |
| Alert storage | SQLite via SQLAlchemy |

---

## Project Structure

```
anomaly-detection-mvp/
│
├── main.py                   # FastAPI app + route definitions
├── db.py                     # SQLAlchemy setup + alert model
├── requirements.txt
│
├── alerts/
│   └── alert_engine.py       # Alert generation + persistence logic
│
├── features/
│   ├── build_features.py     # Offline feature construction
│   └── realtime_features.py  # Live feature extraction per request
│
├── scoring/
│   ├── realtime_scoring.py   # Inference pipeline
│   └── risk_scoring.py       # Threshold-based risk classification
│
├── models/                   # Serialised model artifacts (.pkl)
├── templates/
│   └── index.html            # Chart.js dashboard UI
├── Data/
│   └── transactions.csv      # Sample dataset
└── alerts.db                 # SQLite alert store
```

---

## API Reference

### `POST /score_transaction`

Score a single transaction in real time.

**Request**
```json
{
  "amount": 12000,
  "country": "IN",
  "merchant_category": "electronics",
  "hour_of_day": 2
}
```

**Response**
```json
{
  "risk_score": 0.91,
  "risk_level": "HIGH",
  "alert_triggered": true,
  "features_used": ["amount_zscore", "hour_anomaly", "country_risk_tier"]
}
```

### `GET /`

Interactive dashboard — live risk monitoring, alert history, score distribution chart.

### `GET /alerts`

Returns paginated alert history from SQLite.

---

## Quickstart

```bash
git clone https://github.com/your-username/anomaly-detection-mvp
cd anomaly-detection-mvp

python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

pip install -r requirements.txt

uvicorn main:app --reload
```

Open `http://127.0.0.1:8000` for the dashboard.
Open `http://127.0.0.1:8000/docs` for the auto-generated API docs.

---

## Tech Stack

| Layer | Technology |
|---|---|
| API | FastAPI + Uvicorn |
| ML | Scikit-learn (Isolation Forest), PyOD |
| Feature Engineering | Pandas, NumPy |
| Database | SQLite + SQLAlchemy |
| Dashboard | Jinja2 + Chart.js |

---

## Limitations & Known Issues

- Model trained on a single static dataset — no retraining pipeline yet. Concept drift will degrade performance over time.
- Feature set is limited to amount, country, merchant category, and time. Real fraud systems use 100+ features including device fingerprinting, behavioural sequence, and graph-based signals.
- SQLite is not suitable for high-throughput production. Would swap for PostgreSQL with a connection pool for anything beyond prototyping.
- No authentication on API endpoints — not production-ready as-is.

---

## Roadmap

- [ ] Docker + docker-compose setup for one-command deployment
- [ ] AWS EC2 / Lambda deployment with public endpoint
- [ ] Model explainability — per-transaction feature contribution (SHAP)
- [ ] Batch scoring endpoint for bulk CSV input
- [ ] Model retraining pipeline with MLflow experiment tracking
- [ ] PostgreSQL migration for production-scale alert storage

---

## License

MIT
