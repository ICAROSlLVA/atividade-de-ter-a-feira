"""Apresente os primeiros 15 termos de Fibonacci."""

anterior, atual = 0, 1
for _ in range(15):
    print(anterior)
    anterior, atual = atual, anterior + atual
