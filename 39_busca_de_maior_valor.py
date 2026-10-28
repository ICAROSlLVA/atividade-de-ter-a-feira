"""Encontre maior valor e indice em vinte numeros sem max()."""

numeros = []
for indice in range(1, 21):
    numeros.append(int(input(f"Digite o {indice}o numero: ")))

maior = numeros[0]
indice_maior = 0
for indice in range(1, len(numeros)):
    if numeros[indice] > maior:
        maior = numeros[indice]
        indice_maior = indice
print(f"Maior valor: {maior}; indice: {indice_maior}")
