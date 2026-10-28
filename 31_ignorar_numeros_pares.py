"""Use continue para apresentar somente impares de 1 a 100."""

for numero in range(1, 101):
    if numero % 2 == 0:
        continue
    print(numero)
