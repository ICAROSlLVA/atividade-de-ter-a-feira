"""Repita a leitura ate receber um inteiro positivo."""

numero = int(input("Digite um inteiro positivo: "))
while numero <= 0:
    numero = int(input("Valor invalido. Digite um inteiro positivo: "))
print(f"Numero aceito: {numero}")
