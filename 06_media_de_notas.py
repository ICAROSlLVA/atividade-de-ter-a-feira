"""Leia notas ate -1 e calcule a media das notas informadas."""

soma = 0.0
quantidade = 0
while True:
    nota = float(input("Digite uma nota (-1 para encerrar): "))
    if nota == -1:
        break
    soma += nota
    quantidade += 1

if quantidade:
    print(f"Media das notas: {soma / quantidade:.2f}")
else:
    print("Nenhuma nota foi informada; nao ha media a calcular.")
