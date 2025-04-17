from indicators import calculate_ema, calculate_rsi

def apply_strategy(df):
    df['ema'] = calculate_ema(df)
    df['rsi'] = calculate_rsi(df)
    df['signal'] = 'HOLD'
    df.loc[(df['price'] > df['ema']) & (df['rsi'] < 30), 'signal'] = 'BUY'
    df.loc[(df['price'] < df['ema']) & (df['rsi'] > 70), 'signal'] = 'SELL'
    return df