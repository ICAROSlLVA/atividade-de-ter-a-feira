"""Pesquise um nome em uma lista com dez alunos."""

alunos = []
for indice in range(1, 11):
    alunos.append(input(f"Nome do aluno {indice}: ").strip())
procurado = input("Nome a pesquisar: ").strip()

if any(nome.casefold() == procurado.casefold() for nome in alunos):
    print("Aluno cadastrado.")
else:
    print("Aluno nao cadastrado.")
