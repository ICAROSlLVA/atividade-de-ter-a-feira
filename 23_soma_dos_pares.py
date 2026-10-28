"""Some os numeros pares entre 1 e 100."""

soma = 0
for numero in range(2, 101, 2):
    soma += numero
print(f"Soma dos pares de 1 a 100: {soma}")
