# -*- coding: utf-8 -*-

# É dado um array A consistindo de N inteiros. Rotação do array significa que
# cada elemento é deslocado para a direita por um índice, e o ultimo elemento 
# do array é movido para o primeiro lugar. Por exemplo, a rotação do array
# A = [3, 8, 9, 7, 6] é [6, 3, 8, 9, 7] (elementos são deslocados para direita
# por 1 índice e o 6 é movido para o primeiro lugar)
# 
# O objetivo é rotacionar o array A K tantas vezes; é isso, cada elemento da A
# será deslocado para a direita K vezes. 
# 
# Escreva a função:
#     def solution(A, K)
#
# nisso, dê um array A consistindo de N inteiros e um inteiro K, retorne um
# array A rotacionado K vezes.
#
# Por exemplo:
#
# A = [3, 8, 9, 7, 6]
# K = 3
#
# a função deverá retornar [9, 7, 6, 3, 8]. Tres rotações são necessárias:
#
# [3, 8, 9, 7, 6] -> [6, 3, 8, 9, 7]
# [6, 3, 8, 9, 7] -> [7, 6, 3, 8, 9]
# [7, 6, 3, 8, 9] -> [9, 7, 6, 3, 8]
#
# Outro exemplo, dado
# A = [0, 0, 0]
# K = 1
#
# a função deverá retornar [0, 0, 0]
#
# Dado:
# A = [1, 2, 3, 4]
# K = 4
#
# # a função deverá retornar [1, 2, 3, 4]
#
# Assume que:
#
# - N e K são inteiros dentro de uma faixa [0..100];
# - cada elemento do aaray A é um inteiro dentro de uma faixa [−1,000..1,000].
#
# Na sua solução, concentre na correção. O desempenho da sua solução não será 
# o focus da avaliação.

def solution(A, K):

    if len(A) == 0 or len(A) == 1:
        return A

    while K > 0:
        temp = []
    
        for i in range(len(A)):
            if i == 0:
                last_item = A[len(A) - 1]
                temp.append(last_item)

            else:
                temp.append(A[i - 1])

        K -= 1
        A = temp

    return A