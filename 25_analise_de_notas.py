"""Leia dez notas e apresente maior, menor e media da turma."""

notas = []
for indice in range(1, 11):
    notas.append(float(input(f"Nota do aluno {indice}: ")))

print(f"Maior nota: {max(notas):g}")
print(f"Menor nota: {min(notas):g}")
print(f"Media da turma: {sum(notas) / len(notas):.2f}")
