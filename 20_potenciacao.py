"""Calcule potencia com multiplicacoes sucessivas, sem usar **."""

base = float(input("Digite a base: "))
expoente = int(input("Digite um expoente inteiro nao negativo: "))
while expoente < 0:
    expoente = int(input("Expoente invalido. Digite um inteiro nao negativo: "))

resultado = 1
for _ in range(expoente):
    resultado *= base
print(f"Resultado: {resultado:g}")
