import pandas as pd
import matplotlib.pyplot as plt
from strategy import apply_strategy

df = pd.read_csv("sample_data.csv", parse_dates=["timestamp"])
df = apply_strategy(df)

plt.plot(df['timestamp'], df['price'], label='Цена')
plt.scatter(df[df['signal'] == 'BUY']['timestamp'], df[df['signal'] == 'BUY']['price'], color='green', marker='^', label='BUY')
plt.scatter(df[df['signal'] == 'SELL']['timestamp'], df[df['signal'] == 'SELL']['price'], color='red', marker='v', label='SELL')
plt.xlabel('Дата')
plt.ylabel('Цена')
plt.title('Сигналы на графике цены')
plt.legend()
plt.grid()
plt.show()