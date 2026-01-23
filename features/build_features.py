import pandas as pd
import numpy as np

def build_features(path):
    df = pd.read_csv(path)
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    df['hour'] = df['timestamp'].dt.hour
    df['log_amount'] = np.log1p(df['amount'])

    df['user_mean'] = df.groupby('user_id')['amount'].transform('mean')
    df['user_std'] = df.groupby('user_id')['amount'].transform('std').fillna(1)

    df['amount_zscore'] = (df['amount'] - df['user_mean']) / df['user_std']

    df['device_change'] = (
        df.groupby('user_id')['device_type']
        .transform(lambda x: x != x.shift(1))
        .fillna(False)
        .astype(int)
    )

    features = df[['log_amount', 'amount_zscore', 'hour', 'device_change']]
    return df, features
