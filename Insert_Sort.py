


import random


def ordenacao_selecao(A):

    n = len(A)

    # Percorre o arranjo A
    for j in range(1, n):

        chave = A[j]
        i = j - 1

        # Insere o elemento A[j] na posição correta.

        while i >= 0 and A[i] > chave:

            A[i + 1] = A[i]

            i = i - 1
        A[i + 1] = chave






A = random.sample(range(-10,10), 10)

print("Arranjo não Ordenado: ", A)

ordenacao_selecao(A)

print("Arranjo Ordenado: ", A)