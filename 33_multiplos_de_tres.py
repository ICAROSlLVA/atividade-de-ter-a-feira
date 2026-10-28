"""Apresente de 1 a 100, ignorando multiplos de tres com continue."""

for numero in range(1, 101):
    if numero % 3 == 0:
        continue
    print(numero)
