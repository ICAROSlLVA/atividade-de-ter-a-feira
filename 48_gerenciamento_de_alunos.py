"""Cadastro, medias e busca linear de alunos em um menu."""

alunos = []
while True:
    print("\n1 - Cadastrar aluno\n2 - Listar alunos e medias\n3 - Pesquisar aluno\n0 - Sair")
    opcao = input("Escolha: ")
    if opcao == "0":
        break
    if opcao == "1":
        nome = input("Nome do aluno: ").strip()
        if not nome:
            print("O nome nao pode ficar vazio.")
            continue
        notas = []
        for indice in range(1, 4):
            notas.append(float(input(f"Nota {indice}: ")))
        alunos.append({"nome": nome, "notas": notas})
        print("Aluno cadastrado.")
    elif opcao == "2":
        if not alunos:
            print("Nenhum aluno cadastrado.")
        for aluno in alunos:
            media = sum(aluno["notas"]) / len(aluno["notas"])
            print(f"{aluno['nome']}: media {media:.2f}")
    elif opcao == "3":
        procurado = input("Nome para pesquisar: ").strip().casefold()
        encontrado = None
        for aluno in alunos:
            if aluno["nome"].casefold() == procurado:
                encontrado = aluno
                break
        if encontrado is None:
            print("Aluno nao encontrado.")
        else:
            media = sum(encontrado["notas"]) / len(encontrado["notas"])
            print(f"{encontrado['nome']}: notas {encontrado['notas']}, media {media:.2f}")
    else:
        print("Opcao invalida.")
