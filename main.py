from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

templates = Jinja2Templates(directory="templates")




app = FastAPI(title="Anomaly Detection MVP")

@app.post("/score_transaction")
def score(tx: dict):
    score = score_transaction(tx)
    level = risk_level(score)

    if level == "HIGH":
        db = SessionLocal()
        alert = Alert(risk_score=score, risk_level=level)
        db.add(alert)
        db.commit()
        db.close()

    return {
        "risk_score": score,
        "risk_level": level,
        "alert": level == "HIGH"
    }
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
