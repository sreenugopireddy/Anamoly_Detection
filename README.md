# 🚨 Anomaly Detection System (FastAPI + ML)

A modular, real-time Anomaly Detection System that scores financial transactions, assigns risk levels, and generates alerts through an API-driven architecture with a browser dashboard.

This project demonstrates applied machine learning deployment using FastAPI, feature engineering pipelines, anomaly scoring, and alert storage with a database backend.

---

# 📌 Features

- ✅ Real-time transaction risk scoring
- ✅ Anomaly detection using ML models (scikit-learn / PyOD)
- ✅ Feature engineering pipeline
- ✅ Risk classification (LOW / MEDIUM / HIGH)
- ✅ FastAPI REST endpoints
- ✅ Interactive web UI dashboard
- ✅ Alert generation for high-risk events
- ✅ SQLite alert logging via SQLAlchemy
- ✅ Modular project structure
- ✅ Ready for academic submission or portfolio use

---

# 🏗️ System Architecture

```
Transaction Input
      ↓
Feature Engineering
      ↓
Anomaly / Risk Scoring
      ↓
Risk Classification
      ↓
Alert Engine
      ↓
Database Storage
      ↓
API Response + Dashboard Display
```

---

# 📂 Project Structure

```text
anomaly-detection-mvp/
│
├── main.py                  # FastAPI app entrypoint
├── db.py                    # Database connection setup
├── requirements.txt
│
├── alerts/
│   └── alert_engine.py      # Alert generation logic
│
├── features/
│   ├── build_features.py
│   └── realtime_features.py # Live feature extraction
│
├── scoring/
│   ├── realtime_scoring.py
│   └── risk_scoring.py      # Risk score + thresholds
│
├── models/                  # Saved ML models (.pkl)
│
├── templates/
│   └── index.html           # Web dashboard UI
│
├── Data/
│   └── transactions.csv     # Sample dataset
│
└── alerts.db                # SQLite alerts database
```

---

# 🧠 ML / Detection Approach

The system uses anomaly detection techniques to identify unusual transaction behavior.

Possible models supported:

- Isolation Forest
- Local Outlier Factor
- PyOD detectors
- Statistical risk scoring
- Threshold-based anomaly scoring

Risk score is converted into:

- LOW
- MEDIUM
- HIGH

High-risk transactions trigger alert records in the database.

---

# ⚙️ Requirements

From `requirements.txt`:

```
pandas
numpy
scikit-learn
pyod
fastapi
uvicorn
joblib
sqlalchemy
```

---

# 🚀 Installation

## 1️⃣ Clone the repository

```bash
git clone <your-repo-url>
cd anomaly-detection-mvp
```

---

## 2️⃣ Create virtual environment

```bash
python -m venv venv
```

Activate:

**Windows**
```bash
venv\Scripts\activate
```

**Mac/Linux**
```bash
source venv/bin/activate
```

---

## 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

Server runs at:

```
http://127.0.0.1:8000
```

Open in browser to access dashboard UI.

---

# 🔌 API Endpoints

## Score Transaction

**POST** `/score_transaction`

### Request Body

```json
{
  "amount": 12000,
  "country": "IN"
}
```

### Response

```json
{
  "risk_score": 0.91,
  "risk_level": "HIGH",
  "alert": true
}
```

---

## Home Dashboard

**GET** `/`

Returns the HTML dashboard UI for interactive testing.

---

# 🗄️ Database

- Uses SQLite
- Managed through SQLAlchemy
- Stores high-risk alerts
- File: `alerts.db`

Example alert record:

```
id | risk_score | risk_level | timestamp
```

---

# 🧪 Example Use Cases

- Fraud detection prototype
- Financial anomaly screening
- Risk scoring engine
- ML deployment demonstration
- Academic ML systems project
- Internship portfolio project

---

# 📊 Academic Value

This project demonstrates:

- Applied anomaly detection
- ML model serving
- Feature engineering pipeline
- API deployment
- Real-time scoring
- Database alert logging
- End-to-end ML system design

Suitable for:

- Final year projects
- Mini projects
- ML deployment coursework
- AI systems demonstrations

---

# 🔮 Future Improvements

- Model explainability (feature contribution)
- Risk reason generation
- Alert analytics dashboard
- Batch scoring endpoint
- User authentication
- Model retraining pipeline
- Docker deployment
- Cloud hosting

---

# 👨‍💻 Tech Stack

- Python
- FastAPI
- Scikit-learn
- PyOD
- Pandas / NumPy
- SQLAlchemy
- Uvicorn
- Jinja2 Templates

---

# 📜 License

Academic / educational use recommended. Modify as needed.

---

