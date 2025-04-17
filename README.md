# 📈 Quant Strategy Project #1 — EMA + RSI + Supertrend

## 🔍 Описание

В этом проекте реализован простой алгоритм генерации торговых сигналов с использованием трёх индикаторов:
- 📏 EMA (экспоненциальная скользящая)
- 💪 RSI (индекс относительной силы)
- 💡 Supertrend

Сигналы: **BUY**, **SELL**, **HOLD**

## 🧠 Логика стратегии

- BUY: RSI < 30 и цена выше Supertrend и выше EMA
- SELL: RSI > 70 и цена ниже Supertrend и ниже EMA
- Иначе — HOLD

## 🛠️ Как запустить

```bash
# Проверка сигнала:
python test_signals.py

# Построение графика:
python plot_signals.py
