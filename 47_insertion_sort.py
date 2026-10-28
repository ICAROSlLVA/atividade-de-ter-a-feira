"""Ordene inteiros com Insertion Sort e mostre cada insercao."""

numeros = []
quantidade = int(input("Quantos numeros deseja ordenar? "))
while quantidade < 0:
    quantidade = int(input("A quantidade nao pode ser negativa. Informe novamente: "))
for indice in range(1, quantidade + 1):
    numeros.append(int(input(f"Digite o {indice}o numero: ")))

for indice in range(1, len(numeros)):
    valor = numeros[indice]
    posicao = indice - 1
    while posicao >= 0 and numeros[posicao] > valor:
        numeros[posicao + 1] = numeros[posicao]
        posicao -= 1
    numeros[posicao + 1] = valor
    print(f"Apos insercao: {numeros}")
print(f"Lista ordenada: {numeros}")
