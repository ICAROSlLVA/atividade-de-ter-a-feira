"""Calcule o fatorial de um inteiro nao negativo usando while."""

numero = int(input("Digite um inteiro nao negativo: "))
while numero < 0:
    numero = int(input("Valor invalido. Digite um inteiro nao negativo: "))

fatorial = 1
contador = 1
while contador <= numero:
    fatorial *= contador
    contador += 1

print(f"{numero}! = {fatorial}")
