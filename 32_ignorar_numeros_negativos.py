"""Leia dez inteiros, ignore negativos e some os demais."""

soma = 0
for indice in range(1, 11):
    numero = int(input(f"Digite o {indice}o inteiro: "))
    if numero < 0:
        continue
    soma += numero
print(f"Soma dos valores nao negativos: {soma}")
