"""Leia cinco notas, calcule a media e informe a aprovacao."""

notas = []
for indice in range(1, 6):
    notas.append(float(input(f"Digite a {indice}a nota: ")))

media = sum(notas) / len(notas)
print(f"Media: {media:.2f}")
print("Aprovado." if media >= 7 else "Reprovado.")
