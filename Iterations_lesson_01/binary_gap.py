# -*- coding: utf-8 -*-

# Uma lacuba binária (binary gap) dentro de números positivos inteiros N é
# qualquer sequência máxima consecutiva de zeros que é rodeado por 1 nas
# extremidades na representação binária de N.
#
# Por exemplo, número 9 tem representação binária 1001 e contêm uma lacuna
# binária de tamanho 2. O numero 529 tem representação binária 1000010001 e
# contêm 2 lacunas binárias: uma de tamanho 4 e uma de tamanho 3. O número 20
# tem representação binária 10100 e contêm 1 uma lacuna binária de tamanho 1.
# O número 15 tem representação binária 1111 e não tem lacunas binária.
# O número 32 tem representação binária 100000 e não tem lacunas binária.
#
# Escreva a função:
#     def solution(N)
#
# esta, dê um inteiro positivo N, retorne o tamanho da maior lacuna binária. A
# função deve retornar 0 se N não contêm uma lacuna binária.
#
# Por exemplo, dado N = 1041 a função deve retornar 5, porque N tem
# representação binária 10000010001 e então sua maior lacuna binária é de
# tamanho 5. Dado N = 32 a função deve retornar 0, porque N tem representação
# binária 100000 e portanto sem lacuna binária.
#
# Escreva um eficiente algoritmo para as seguintes suposições:
# - N é um inteiro dentro de uma faixa [1..2,147,483,647].

def solution(N):
    one_indexes = []
    counter_list = []
  
    binary_number = bin(N).replace('0b', '')
  
    for item in range(len(binary_number)):
        if binary_number[item] == '1':
            one_indexes.append(item)
  
    for item in range(len(one_indexes)):
        if len(one_indexes) == 1:
            return 0

        if item == len(one_indexes) - 1:
            break

        counter = one_indexes[item + 1] - one_indexes[item] - 1

        counter_list.append(counter)
  
    return max(counter_list)




    
