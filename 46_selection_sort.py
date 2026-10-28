"""Ordene uma lista de inteiros com Selection Sort."""

numeros = [29, 10, 14, 37, 13, 5, 42, 8]
print(f"Lista inicial: {numeros}")
for inicio in range(len(numeros) - 1):
    indice_menor = inicio
    for indice in range(inicio + 1, len(numeros)):
        if numeros[indice] < numeros[indice_menor]:
            indice_menor = indice
    numeros[inicio], numeros[indice_menor] = numeros[indice_menor], numeros[inicio]
print(f"Ordem crescente: {numeros}")
