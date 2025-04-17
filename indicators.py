import pandas as pd

def calculate_ema(df, span=5):
    return df['price'].ewm(span=span, adjust=False).mean()

def calculate_rsi(df, period=5):
    delta = df['price'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))