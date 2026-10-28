"""Mostre o indice da primeira ocorrencia de um valor em uma lista."""

numeros = [12, 7, 25, 4, 18, 31, 9, 2, 16, 20]
print(f"Lista: {numeros}")
procurado = int(input("Valor a buscar: "))

indice_encontrado = -1
for indice, numero in enumerate(numeros):
    if numero == procurado:
        indice_encontrado = indice
        break
if indice_encontrado >= 0:
    print(f"Valor encontrado no indice {indice_encontrado}.")
else:
    print("Valor nao encontrado.")
