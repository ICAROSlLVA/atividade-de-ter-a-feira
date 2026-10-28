"""Cadastre, busque e ordene produtos com menu e estruturas de repeticao."""

produtos = []
while True:
    print("\n1 - Cadastrar produto\n2 - Buscar produto\n3 - Listar em ordem alfabetica\n0 - Sair")
    opcao = input("Escolha: ")
    if opcao == "0":
        break
    if opcao == "1":
        nome = input("Nome do produto: ").strip()
        if not nome:
            print("Nome vazio ignorado.")
            continue
        quantidade = int(input("Quantidade: "))
        if quantidade < 0:
            print("A quantidade nao pode ser negativa.")
            continue
        produtos.append({"nome": nome, "quantidade": quantidade})
        print("Produto cadastrado.")
    elif opcao == "2":
        procurado = input("Nome para buscar: ").strip().casefold()
        encontrado = None
        for produto in produtos:
            if produto["nome"].casefold() == procurado:
                encontrado = produto
                break
        if encontrado is None:
            print("Produto nao encontrado.")
        else:
            print(f"{encontrado['nome']}: {encontrado['quantidade']} unidade(s)")
    elif opcao == "3":
        ordenados = produtos.copy()
        for indice in range(1, len(ordenados)):
            item = ordenados[indice]
            posicao = indice - 1
            while posicao >= 0 and ordenados[posicao]["nome"].casefold() > item["nome"].casefold():
                ordenados[posicao + 1] = ordenados[posicao]
                posicao -= 1
            ordenados[posicao + 1] = item
        if not ordenados:
            print("Nenhum produto cadastrado.")
        for produto in ordenados:
            print(f"{produto['nome']}: {produto['quantidade']} unidade(s)")
    else:
        print("Opcao invalida.")
