"""Leia inteiros ate zero e mostre o maior valor diferente de zero."""

maior = None

while True:
    numero = int(input("Digite um numero inteiro (0 para encerrar): "))
    if numero == 0:
        break
    if maior is None or numero > maior:
        maior = numero

if maior is None:
    print("Nenhum numero diferente de zero foi informado.")
else:
    print(f"Maior numero informado: {maior}")
