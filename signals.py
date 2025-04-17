import pandas as pd
from strategy import apply_strategy

def generate_signal(csv_file):
    df = pd.read_csv(csv_file, parse_dates=["timestamp"])
    df = apply_strategy(df)
    last_signal = df.iloc[-1]['signal']
    return last_signal