"""Analise e pesquise vinte inteiros por busca linear e binaria."""

numeros = []
for indice in range(1, 21):
    numeros.append(int(input(f"Digite o {indice}o numero: ")))

while True:
    print("\n1 - Media\n2 - Maior e menor\n3 - Ordem crescente e decrescente")
    print("4 - Buscar numero (linear e binaria)\n0 - Sair")
    opcao = input("Escolha: ")
    if opcao == "0":
        break
    if opcao == "1":
        print(f"Media: {sum(numeros) / len(numeros):.2f}")
    elif opcao == "2":
        maior = menor = numeros[0]
        for numero in numeros[1:]:
            if numero > maior:
                maior = numero
            if numero < menor:
                menor = numero
        print(f"Maior: {maior}; menor: {menor}")
    elif opcao == "3":
        crescente = sorted(numeros)
        print(f"Crescente: {crescente}")
        print(f"Decrescente: {crescente[::-1]}")
    elif opcao == "4":
        procurado = int(input("Numero a pesquisar: "))
        comparacoes_lineares = 0
        encontrado_linear = False
        for numero in numeros:
            comparacoes_lineares += 1
            if numero == procurado:
                encontrado_linear = True
                break

        ordenados = sorted(numeros)
        inicio, fim = 0, len(ordenados) - 1
        comparacoes_binarias = 0
        encontrado_binario = False
        while inicio <= fim:
            meio = (inicio + fim) // 2
            comparacoes_binarias += 1
            if ordenados[meio] == procurado:
                encontrado_binario = True
                break
            if ordenados[meio] < procurado:
                inicio = meio + 1
            else:
                fim = meio - 1
        print(f"Busca linear: {'encontrado' if encontrado_linear else 'nao encontrado'}, "
              f"{comparacoes_lineares} comparacao(oes).")
        print(f"Busca binaria: {'encontrado' if encontrado_binario else 'nao encontrado'}, "
              f"{comparacoes_binarias} comparacao(oes).")
    else:
        print("Opcao invalida.")
