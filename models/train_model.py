from sklearn.ensemble import IsolationForest
from features.build_features import build_features
import joblib

def train():
    df, X = build_features("data/transactions.csv")

    model = IsolationForest(
        n_estimators=200,
        contamination=0.15,
        random_state=42
    )

    model.fit(X)
    joblib.dump(model, "models/isolation_forest.pkl")
    print("Model trained and saved.")

if __name__ == "__main__":
    train()




