"""Localize um valor com busca binaria em uma lista ordenada de vinte."""

numeros = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44, 47, 50, 53, 56, 59]
procurado = int(input(f"Valor a buscar em {numeros}: "))
inicio = 0
fim = len(numeros) - 1
encontrado = False

while inicio <= fim:
    meio = (inicio + fim) // 2
    if numeros[meio] == procurado:
        encontrado = True
        break
    if numeros[meio] < procurado:
        inicio = meio + 1
    else:
        fim = meio - 1

print("Valor encontrado." if encontrado else "Valor nao encontrado.")
