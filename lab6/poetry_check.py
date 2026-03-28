import requests
import sys

print("\n=== Перевірка середовища Poetry ===")
print(f"Версія Python: {sys.version.split()[0]}")
print(f"Версія requests: {requests.__version__}")
print(f"Шлях до VENV: {sys.prefix}")
print("==================================\n")