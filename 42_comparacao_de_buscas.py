"""Compare o numero de comparacoes da busca linear e binaria."""

numeros = list(range(2, 41, 2))
procurado = int(input(f"Valor a localizar na lista {numeros}: "))

comparacoes_lineares = 0
for numero in numeros:
    comparacoes_lineares += 1
    if numero == procurado:
        break

inicio, fim = 0, len(numeros) - 1
comparacoes_binarias = 0
while inicio <= fim:
    meio = (inicio + fim) // 2
    comparacoes_binarias += 1
    if numeros[meio] == procurado:
        break
    if numeros[meio] < procurado:
        inicio = meio + 1
    else:
        fim = meio - 1

print(f"Busca linear: {comparacoes_lineares} comparacao(oes).")
print(f"Busca binaria: {comparacoes_binarias} comparacao(oes).")
