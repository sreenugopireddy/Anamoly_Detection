import numpy as np
import pandas as pd

def build_realtime_features(tx):
    df = pd.DataFrame([tx])

    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["hour"] = df["timestamp"].dt.hour
    df["log_amount"] = np.log1p(df["amount"])

    # MVP assumptions
    df["amount_zscore"] = 0
    df["device_change"] = 0

    return df[["log_amount", "amount_zscore", "hour", "device_change"]]
