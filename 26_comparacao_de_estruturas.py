"""Mostre 1 a 20 com for e while e explique as implementacoes."""

print("Usando for:")
for numero in range(1, 21):
    print(numero)

print("\nUsando while:")
numero = 1
while numero <= 20:
    print(numero)
    numero += 1

print("\nO for percorre diretamente uma sequencia de valores.")
print("O while repete enquanto a condicao for verdadeira e exige atualizar o contador.")
