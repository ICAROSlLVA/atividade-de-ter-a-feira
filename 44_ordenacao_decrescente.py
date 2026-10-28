"""Ordene quinze inteiros em ordem decrescente com sort()."""

numeros = []
for indice in range(1, 16):
    numeros.append(int(input(f"Digite o {indice}o numero: ")))
numeros.sort(reverse=True)
print(f"Ordem decrescente: {numeros}")
