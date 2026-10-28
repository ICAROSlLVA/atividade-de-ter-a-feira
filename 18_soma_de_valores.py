"""Leia dez inteiros e apresente a soma."""

soma = 0
for indice in range(1, 11):
    soma += int(input(f"Digite o {indice}o numero inteiro: "))
print(f"Soma total: {soma}")
