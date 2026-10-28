"""Solicite a senha ate que a senha correta seja informada."""

while True:
    senha = input("Digite a senha: ")
    if senha == "python123":
        break

print("Acesso autorizado.")
