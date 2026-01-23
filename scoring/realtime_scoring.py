import joblib
from features.realtime_features import build_realtime_features

model = joblib.load("models/isolation_forest.pkl")

def score_transaction(tx):
    X = build_realtime_features(tx)
    raw = -model.decision_function(X)[0]
    score = min(100, max(0, raw * 100))
    return int(score)
