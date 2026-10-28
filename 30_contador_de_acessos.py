"""Permita tres tentativas de autenticacao antes de bloquear o acesso."""

senha_correta = "python123"
for tentativa in range(1, 4):
    senha = input(f"Senha (tentativa {tentativa}/3): ")
    if senha == senha_correta:
        print("Acesso autorizado.")
        break
else:
    print("Acesso bloqueado.")
