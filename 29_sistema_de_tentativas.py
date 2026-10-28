"""Adivinhe o numero secreto 13, entre 1 e 20."""

secreto = 13
while True:
    tentativa = int(input("Adivinhe o numero secreto (1 a 20): "))
    if tentativa == secreto:
        print("Acertou!")
        break
    if tentativa < secreto:
        print("O numero secreto e maior.")
    else:
        print("O numero secreto e menor.")
