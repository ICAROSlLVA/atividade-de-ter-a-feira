"""Ordene dez inteiros com Bubble Sort, sem sort() ou sorted()."""

numeros = []
for indice in range(1, 11):
    numeros.append(int(input(f"Digite o {indice}o numero: ")))

for fim in range(len(numeros) - 1, 0, -1):
    houve_troca = False
    for indice in range(fim):
        if numeros[indice] > numeros[indice + 1]:
            numeros[indice], numeros[indice + 1] = numeros[indice + 1], numeros[indice]
            houve_troca = True
    if not houve_troca:
        break
print(f"Ordem crescente: {numeros}")
