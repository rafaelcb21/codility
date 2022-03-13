# -*- coding: utf-8 -*-

# É dado um array não vazia A consistindo de N inteiros. O array contem um
# número impar de elementos, e cada elemento do array podes ser pareado com
# outro elemento que contem o mesmo valor, exceto por um elemento que é
# deixado sem par.
#
# Por exemplo, no array A tal que:
#
# A[0] = 9  A[1] = 3  A[2] = 9
# A[3] = 3  A[4] = 9  A[5] = 7
# A[6] = 9
#
# - os elementos nos indexes 0 e 2 tem valor 9
# - os elementos nos indexes 1 e 3 tem valor 3
# - os elementos nos indexes 4 e 6 tem valor 9
# - o elemento no index 5 tem valor 7 e não tem par
#
# Escreva a função:
#
# def solution(A)
#
# que, dado um array A constituindo de N inteiros cumprindo as condições acima
# retorne o valor do elemento sem par.
#
# Por exemplo, no array A tal que:
#
# A[0] = 9  A[1] = 3  A[2] = 9
# A[3] = 3  A[4] = 9  A[5] = 7
# A[6] = 9
#
# a função deve retornar 7, como é explicado no exemplo acima.
#
# Escreva um algoritmo eficiente para as seguintes suposições
#
# - N é um numero impar dentro de uma faixa [1..1,000,000];
# - cada elemento do array A é um inteiro dentro de uma faixa [1..1,000,000,000];
# - todos os valores de A ocorrem um numero par de vezes, com exceção de 1 numero

def solution(A):

    list_sort = sorted(A)

    if len(A) == 1:
        return A[0]
        
    for i in range(0, len(list_sort), 2):
        if i + 1 == len(list_sort):
            return list_sort[i] # ultimo numero

        if list_sort[i] != list_sort[i + 1]:
            return list_sort[i]

# Solução com XOR
# XOR é um operador lógico que seu resultado só será verdadeiro se os itens
# forem diferentes, caso os itens sejam iguais, o resultado será falso = ZERO
#
# Se existe um array de tamanho par, sendo que todos os elementos possuem um
# numero pareado, ao utilizar o operador logico XOR, o resultado será ZERO
# 
# Se existir mais do que um número sem um par, o XOR retornará o valor da operação
# XOR ao longo dos elemento do array, o que deixa imprevisivel o resultado, pois
# o array pode ser gerado de forma randomica, não sabendo assim qual será
# a valor do XOR com o ultimo número do array
# 
# Mas se existir somente 1 numero sem par, o resultado final da operação XOR
# será o numero que não tem par, já que todos os numeros serão false (ZERO)
# como exceção dounico número sem par.
#
# Quando se começa com o 'result = 0' ele garantirá que o primeiro valor será 
# igual o do primeiro elmento comparado.
#
# A prova disso o que foi dito, estará nos testes.

def solution2(A):
   result = 0
   for number in A:
     result ^= number

   return result
