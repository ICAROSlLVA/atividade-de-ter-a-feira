"""Registre retiradas sem permitir que o estoque fique negativo."""

estoque = int(input("Quantidade inicial de produtos (>= 0): "))
while estoque < 0:
    estoque = int(input("Quantidade invalida. Informe um valor >= 0: "))

while estoque > 0:
    print(f"Estoque atual: {estoque}")
    retirada = int(input("Quantidade a retirar: "))
    if retirada <= 0:
        print("A retirada deve ser positiva.")
    elif retirada > estoque:
        print("Retirada superior ao estoque disponivel.")
    else:
        estoque -= retirada
print(f"Estoque final: {estoque}")
