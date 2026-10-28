"""Apresente a tabuada de multiplicacao de 1 a 10 usando while."""

numero = int(input("Digite um numero inteiro: "))
multiplicador = 1
while multiplicador <= 10:
    print(f"{numero} x {multiplicador} = {numero * multiplicador}")
    multiplicador += 1
