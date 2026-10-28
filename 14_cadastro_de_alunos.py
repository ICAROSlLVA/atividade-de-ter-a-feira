"""Cadastre nomes de alunos enquanto o usuario desejar continuar."""

alunos = []
while True:
    nome = input("Nome do aluno: ").strip()
    if nome:
        alunos.append(nome)
    else:
        print("O nome nao pode ficar vazio.")
    continuar = input("Deseja cadastrar outro aluno? (s/n): ").strip().lower()
    if continuar != "s":
        break

print(f"Alunos cadastrados ({len(alunos)}):")
for aluno in alunos:
    print(aluno)
