"""Leia dez notas, ignore as invalidas e calcule a media das validas."""

notas_validas = []
for indice in range(1, 11):
    nota = float(input(f"Digite a {indice}a nota: "))
    if nota < 0 or nota > 10:
        continue
    notas_validas.append(nota)

if notas_validas:
    print(f"Media das notas validas: {sum(notas_validas) / len(notas_validas):.2f}")
else:
    print("Nenhuma nota valida foi informada; nao ha media a calcular.")
