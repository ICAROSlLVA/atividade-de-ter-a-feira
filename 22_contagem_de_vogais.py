"""Conte as vogais de uma palavra usando for."""

palavra = input("Digite uma palavra: ")
vogais = "aeiou"
quantidade = 0
for caractere in palavra.casefold():
    if caractere in vogais:
        quantidade += 1
print(f"Quantidade de vogais: {quantidade}")
