"""Some inteiros informados ate o usuario digitar zero."""

soma = 0
while True:
    numero = int(input("Digite um numero inteiro (0 para encerrar): "))
    if numero == 0:
        break
    soma += numero

print(f"Soma dos numeros informados: {soma}")
