"""Pesquise um valor em uma lista de dez inteiros."""

numeros = []
for indice in range(1, 11):
    numeros.append(int(input(f"Digite o {indice}o numero: ")))
procurado = int(input("Numero a buscar: "))

encontrado = False
for numero in numeros:
    if numero == procurado:
        encontrado = True
        break
print("Numero encontrado." if encontrado else "Numero nao encontrado.")
