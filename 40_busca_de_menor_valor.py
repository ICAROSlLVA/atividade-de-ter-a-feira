"""Encontre menor valor e indice em vinte numeros sem min()."""

numeros = []
for indice in range(1, 21):
    numeros.append(int(input(f"Digite o {indice}o numero: ")))

menor = numeros[0]
indice_menor = 0
for indice in range(1, len(numeros)):
    if numeros[indice] < menor:
        menor = numeros[indice]
        indice_menor = indice
print(f"Menor valor: {menor}; indice: {indice_menor}")
