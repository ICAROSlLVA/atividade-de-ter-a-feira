"""Permita depositos e saques ate que o usuario escolha sair."""

saldo = 0.0
while True:
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("1 - Depositar\n2 - Sacar\n0 - Sair")
    opcao = input("Escolha: ")
    if opcao == "0":
        break
    if opcao not in ("1", "2"):
        print("Opcao invalida.")
        continue
    valor = float(input("Valor: R$ "))
    if valor <= 0:
        print("O valor deve ser positivo.")
    elif opcao == "1":
        saldo += valor
    elif valor > saldo:
        print("Saldo insuficiente.")
    else:
        saldo -= valor
print(f"Saldo final: R$ {saldo:.2f}")
