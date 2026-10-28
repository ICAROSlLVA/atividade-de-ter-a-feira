"""Registre votos 1, 2 ou 3; zero encerra a votacao."""

votos = {1: 0, 2: 0, 3: 0}
while True:
    try:
        voto = int(input("Vote 1, 2 ou 3 (0 para encerrar): "))
    except ValueError:
        print("Digite um numero inteiro.")
        continue
    if voto == 0:
        break
    if voto in votos:
        votos[voto] += 1
    else:
        print("Voto invalido; escolha 1, 2, 3 ou 0.")

for opcao, total in votos.items():
    print(f"Opcao {opcao}: {total} voto(s)")
