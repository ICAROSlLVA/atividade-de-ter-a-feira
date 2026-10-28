"""Leia um inteiro positivo e apresente a contagem regressiva ate zero."""

numero = int(input("Digite um numero inteiro positivo: "))
while numero <= 0:
    numero = int(input("Valor invalido. Digite um inteiro positivo: "))

while numero >= 0:
    print(numero)
    numero -= 1
