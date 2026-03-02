from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from utils.db import SessionLocal, Alert

# -----------------------------
# FastAPI Setup
# -----------------------------
app = FastAPI(title="Anomaly Detection System")
templates = Jinja2Templates(directory="templates")


# -----------------------------
# Request Model (validation)
# -----------------------------
class TxIn(BaseModel):
    amount: float
    country: str


# -----------------------------
# Scoring Logic (replace later with ML)
# -----------------------------
def score_transaction_logic(amount: float) -> float:
    if amount > 10000:
        return 0.9
    elif amount > 5000:
        return 0.6
    else:
        return 0.2


def risk_level(score: float) -> str:
    if score > 0.8:
        return "HIGH"
    elif score > 0.5:
        return "MEDIUM"
    else:
        return "LOW"


# -----------------------------
# Routes
# -----------------------------

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/score_transaction")
def score(tx: TxIn):

    s = score_transaction_logic(tx.amount)
    level = risk_level(s)

    # store HIGH alerts
    if level == "HIGH":
        db = SessionLocal()
        db.add(Alert(risk_score=s, risk_level=level))
        db.commit()
        db.close()

    return {
        "risk_score": s,
        "risk_level": level,
        "alert": level == "HIGH",
        "reasons": _build_reasons(tx.amount)
    }


def _build_reasons(amount: float):
    reasons = []
    if amount > 10000:
        reasons.append("Very high transaction amount")
    elif amount > 5000:
        reasons.append("Above normal transaction range")
    return reasons


@app.get("/alerts_recent")
def alerts_recent():
    db = SessionLocal()
    rows = db.query(Alert).order_by(Alert.id.desc()).limit(20).all()
    db.close()

    return [
        {
            "risk_score": r.risk_score,
            "risk_level": r.risk_level,
            "created_at": str(r.created_at)
        }
        for r in rows
    ]
