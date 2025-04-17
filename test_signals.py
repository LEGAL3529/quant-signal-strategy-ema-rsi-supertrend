from signals import generate_signal
import sys

file = sys.argv[1] if len(sys.argv) > 1 else "sample_data.csv"
signal = generate_signal(file)
print("Сигнал:", signal)