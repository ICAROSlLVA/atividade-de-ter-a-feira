"""Leia dez nomes e apresente os que nao comecam com A."""

nomes = []
for indice in range(1, 11):
    nomes.append(input(f"Nome {indice}: ").strip())

print("Nomes que nao comecam com A:")
for nome in nomes:
    if nome.casefold().startswith("a"):
        continue
    print(nome)
