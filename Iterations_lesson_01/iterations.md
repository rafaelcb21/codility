
# Interações

Na programação, interações significam repetir alguma parte do seu programa. Nesta lição está presente o básico da construção de programação que permite as interações de serem realizadas: ‘for’ e ‘while’ loops (ciclos).

## 1.1. ’For’ loops (ciclos)

Se você quer repetir uma determinada operação de um número durante o tempo, ou repeti-lo para cada elemento de uma coleção, um ‘for’ ciclo é a ferramenta correta. Sua sintaxe é a seguinte:

#### ==1.1: ‘*For*’ sintaxe do ciclo==
 ```python
 1  for alguma_varival in faixa_de_valores:
 2      corpo_do_ciclo
 ```

O ciclo do for repete o *corpo_do_ciclo* para cada valor em turnos que vem da *faixa_de_valores*, com o valor corrente atribuído para *alguma_variavel*. Nesta simples forma, a *faixa_de_valores* pode ser faixa de inteiros, indicado por: *range(mais_baixo, mais_alto + 1)*. Por exemplo, o seguinte ciclo imprime cada inteiro de 0 até 99:

```python
1  for i in range(0, 100):
2      print(i)
```
 Ao percorrer a faixa de valores de números inteiros começando do 0 é uma operação muito comum. (Isto é principalmente porque *arrays* e listas em Python são indexadas por inteiros começando por 0; veja o Capítulo 2 *Arrays* para mais detalhes.) Quando especificamos a faixa de inteiros, se o valor de início é igual a 0 então você pode simplesmente omiti-lo. Por exemplo, o seguinte ciclo produz exatamente o mesmo resultado do exemplo anterior:
 
```python
1  for i in range(100):
2      print(i)
```

**Exemplo:** Nós estamos dando alguns inteiros positivos *n*. Vamos computar o fatorial de *n* e atribuí-lo a variável fatorial. O fatorial de *n* é *n!* = 1 * 2 * 3 * … * n. Nós podemos obter isso iniciando com 1 e multiplicando isso por todos os inteiros de 1 até *n*.

 ```python
1  fatorial = 1
2  for i in range(1, n + 1):
3      fatorial *= i
```  

**Exemplo:** Vamos imprimir um triângulo feito por asteriscos (‘*’) separados por espaços. O triângulo deve consistir de *n* linhas, onde *n* é número inteiro positivo que será fornecido,e as linhas consecutivas devem conter 1, 2, … *n* asteriscos. Por exemplo, para *n* = 4 o triângulo deve aparecer da seguinte forma:

```python
*
* *
* * *
* * * *
```

Nós precisamos usar 2 ciclos, um dentro do outro. O ciclo de fora deve imprimir o número da linha em cada passo, e o ciclo de dentro deve imprimir 1 asterisco para cada passo do ciclo:

```python
1  for i in range(1, n + 1):
2      for j in range(i):
3          print(‘* ’)
4      print
```
 
A função *range* pode aceitar um argumento a mais que são os passos com os quais os valores iterados progridem. Mais formalmente *range(start, stop, step)* é a sequência de valores começando com o *start*, cujo cada valor consecutivo é aumentado pelo *step*, e que contém somente os valores menores que o *stop*. (para *step* positivos; ou maiores do que o *stop* para *step* negativos). Por exemplo, *range(10, 0, -1)* representa a sequência 10, 9, 8,...., 1. Note que nós não omitimos o *start* quando nós especificamos o *step*.

**Exemplo:** Vamos imprimir um triângulo feito de asteriscos (‘*’) separados por espaços e consistindo de *n* linhas novamentes, mas dessa vez de ponta cabeça, e faça isso simetricamente. As linhas consecutivas devem conter 2*n* - 1, 2*n* - 3, …., 3, 1 asteriscos e deve ser identado por 0, 2 ,4,..., 2(*n*-1) espaços. Por exemplo, para *n* = 4 o triângulo deve aparecer como se segue:

 ```python
  * * * * * * *
    * * * * *
      * * *
        *
 ```

O triângulo deve ter *n* linhas, onde *n* é um dado número inteiro positivo.

Desta vez nós usaremos 3 ciclos: 1 externo e 2 internos ciclos. O ciclo externo em cada passo imprimirá 1 linha do triângulo. O primeiro ciclo interno é responsável por imprimir a indentação, e o segundo por imprimir os asteriscos.

```python
1  for i in range(n, 0, -1):
2      for j in range(n - i):
3          print(‘ ’)
4      for j in range(2 * i - 1):
5          print(‘ *’)
6      print
```

#### 1.2. ’While’ loops (ciclos)

O número de passos em um ciclo de for, e os valores sobre os quais nós fazemos os ciclos, são fixados antes do início do ciclo. E se o número de passos não é conhecido antecipadamente, ou os valores sobre os quais fazemos o ciclo são gerados um por um, e portanto não são conhecidos de antemão? Em tal caso, nós temos que usar um diferente tipo de ciclo, chamado de ciclo ‘while’. A sintaxe para o while ciclo é como se segue:

#### ==1.2: ‘While’ sintaxe do ciclo==
```python
1  while alguma_condição:
2      corpo_do_ciclo
```

Antes de cada passo do ciclo, *alguma_condição* é computada. Enquanto esse valor for verdadeiro, o *corpo_do_ciclo* é executado. Uma vez que se torne falso, nós saímos do ciclo sem executar o *corpo_do_ciclo*.

**Exemplo:** Dado um número inteiro positivo n, como nós podemos contar o número de dígitos numa representação decimal? Uma forma de fazer é converter o inteiro em uma string e contar os caracteres. Aqui, no entanto, nós iremos utilizar somente operações aritméticas. Nós podemos simplesmente manter dividindo o número por dez e contar quantos passos são necessários para obtermos o 0.

```python
1  result = 0
2  while n > 0:
3      n = n // 10
4      result += 1
```
  
**Exemplo:** Os números Fibonacci formam uma sequência de inteiros definidos recursivamente da seguinte maneira. Os primeiros 2 números da sequência Fibonacci são 0 e 1, e a cada número subsequente é a soma dos 2 anteriores. Os primeiros poucos elementos na sequência são: 0, 1, 1, 2, 3, 5, 8,13. Vamos escrever um programa que imprima todos os números Fibonaccis, não excedendo um dado número inteiro *n*.

Nós podemos continuar gerando e imprimindo consecutivamente os números Fibonacci até nós ultrapassarmos *n*. Em cada passo basta armazenar somente 2 números consecutivos de Fibonacci.

```python
1  a = 0
2  b = 1
3  while a <= n:
4      print(a)
5      c = a + b
6      a = b
7      b = c
```
  
#### 1.3. Realizando ciclos sobre coleções de valores

Nós temos visto como o ciclo atua sobre inteiros. É possível realizar ciclos sobre valores de outros tipos? Sim: usando um ciclo de *for*, nós podemos realizar ciclos sobre valores armazenados em virtualmente qualquer tipo de container. A função *range* constrói uma lista contendo todos os valores sobre os quais nós devemos realizar o ciclo. Contudo, nós podemos passar uma lista construída de qualquer outra maneira.

**Exemplo:** O seguinte programa

```python
1  days = [’Monday’, ’Tuesday’, ’Wednesday’, ’Thursday’, ’Friday’, ’Saturday’, ’Sunday’]
2  for day in days:
3      print(day)
```
imprime todos os dias da semana, um por linha.

Quando nós usamos a função *range*, nós primeiro construímos uma lista com todos os inteiros sobre os quais nós faremos o ciclo; então nós iniciamos o ciclo. Há um consumo de memória quando realizamos o ciclo sobre uma sequência longa. Em tal caso, é aconselhável usar - ao invés do *range* - uma função equivalente chamada de *xrange*. Esta retorna exatamente a mesma sequência de inteiros, mas ao invés de armazená-los numa lista, ele retorna um objeto que gera-os durante o processo.

Se o seu ciclo atua sobre um conjunto de valores, o corpo do ciclo é executado exatamente uma vez para cada valor no conjunto; contudo, a ordem em que os valores são processados é arbitraria.

**Exemplo:** Se nós modificarmos o programa acima ligeiramente, como se segue:

```python
1  days =set( [’Monday’, ’Tuesday’, ’Wednesday’, ’Thursday’, ’Friday’, ’Saturday’, ’Sunday’])
2  for day in days:
3      print(day)
```

nós podemos obter o resultado dos dias em alguma ordem estranha, por exemplo:
```python
Monday
Tuesday
Friday
Wednesday
Thursday
Sunday
Saturday
```
 
Realizando um ciclo sobre um dicionário, significa fazer um ciclo sobre um conjunto de chaves. Novamente, a ordem em que as chaves são processadas é arbitrário.

**Exemplo:** O seguinte programa:

```python
1  days = {’mon’: ’Monday’, ’tue’: ’Tuesday’, ’wed’: ’Wednesday’, ’thu’: ’Thursday’, ’fri’: ’Friday’, ’sat’: ’Saturday’, ’sun’: ’Sunday’}
2  for day in days:
3 print(day, ’stands for’, days[day]
```

pode produzir como resultado por exemplo:

```
wed stands for Wednesday
sun stands for Sunday
fri stands for Friday
tue stands for Tuesday
mon stands for Monday
thu stands for Thursday
sat stands for Saturday
```