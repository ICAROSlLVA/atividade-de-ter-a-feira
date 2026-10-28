"""Leia dez inteiros e apresente-os em ordem crescente com sorted()."""

numeros = []
for indice in range(1, 11):
    numeros.append(int(input(f"Digite o {indice}o numero: ")))
print(f"Ordem crescente: {sorted(numeros)}")
