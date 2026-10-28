"""Solicite novamente ate receber uma idade entre 0 e 120."""

idade = int(input("Digite a idade (0 a 120): "))
while idade < 0 or idade > 120:
    idade = int(input("Idade invalida. Digite um valor entre 0 e 120: "))

print(f"Idade valida: {idade}")
