import joblib
import numpy as np
from features.build_features import build_features

model = joblib.load("models/isolation_forest.pkl")

_, X = build_features("data/transactions.csv")

raw_scores = -model.decision_function(X)
risk_scores = (raw_scores - raw_scores.min()) / (raw_scores.max() - raw_scores.min())
risk_scores = (risk_scores * 100).astype(int)
