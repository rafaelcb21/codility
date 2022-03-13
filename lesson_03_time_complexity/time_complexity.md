# Complexidade de Tempo

Usando o tempo de complexidade se torna fácil para estimar o tempo de execução de um programa. Executando o calculo preciso do tempo de uma operação de um programa é um processo de trabalho muito intensivo (isso depende do compilador, e do tipo de computador ou da velocidade do processador). Portando, nós não iremos fazer uma medição precisa; somente uma medição de uma certa ordem de magnitude.

Complexidade pode ser vista como o máximo de operações primitivas que um programa pode executar. Oerações Regulares são simples adições, multiplicações e atribuições etc. Nós podemos deixar algumas operações sem contar e concentrar-se nas que são realizadas um grande numero de vezes. Tais como operações que são referidas como *dominantes*.

O número de operações dominantes depende especificamente da entrada dos dados. Nós usualmente queremos saber como o desempenho do tempo depende de um aspecto particular dos dados. Isto é mais frequentemente o tamanho do dado, mas também pode ser o tamanho matriz quadrada ou o valor de entrada de alguma variável.

#### <mark>3.1. Qual é a operação dominante?</mark>
 ```python
 1  def dominant(n):
 2      result = 0
 3      for i in xrange(n):
 4          result += 1
 5      return result
 ```

A operação na linha 4 é dominante e será executada *n* vezes. A complexidade é descrita na notação Big-O: nesse caso O(*n*) - complexidade linear.

A complexidade especifica a ordem de grandeza dentro do qual o programa será realizado nas operações. Mais precisamente, no caso de O(*n*), o programa pode desempenhar *c . n* operações, onde *c* é uma constante; contudo, pode não desempenhar *n<sup>2</sup>* operações, já que isto envolve uma diferente ordem de magnitude de dados. Em otras palavras, quando calculamos acomplexidade nós omitimos as constantes: exemplo, independentemente se o ciclo é executado 20 .*n* vezes ou *n/5* vezes, nós ainda temos a complexidade de O(*n*) mesmo que o tempo de execução do programa possa variar. Quando analisamos a complexidade nós precisamos olhar para o específico, no pior dos casos de exemplos de dados em que o programa terá que gastar muito tempo para processar.

## 3.1. Comparações entre diferentes tempos de complexidades

Vamos comparar algumas complexidades básicas de tempo.

#### <mark>3.2. Tempo constante - O(1)</mark>
 ```python
 1  def constant(n):
 2      result = n * n
 3      return result
 ```
Há sempre um número fixo de operações.

#### <mark>3.3. Tempo logarítmico - O(log *n*)</mark>
 ```python
1   def logarithmic(n):
2       result = 0
3       while n > 1:
4           n //= 2
5           result += 1
6       return result
 ```
O valor de *n* é reduzido pela metade em cada interação do ciclo. Se *n* = 2<sup>*x*</sup> então p log*n* = *x*. Quanto tempo o programa abaixo levará para executar, depende da entrada de dados?

#### <mark>3.4. Tempo linear - O(*n*)</mark>
 ```python
1   def linear(n, A):
2       for i in xrange(n):
3           if A[i] == 0:
4               return 0
5       return 1
 ```
Vamos anotar que se o primeiro valor do array A é 0 então o programa será encerrado imediatamente. Mas lembre-se, quando analisamos o tempo de complexidade nós devemos olhar para o pior cenário. O programa levará muito tempo para executar se o array A não tiver nenhum 0.

#### <mark>3.5. Tempo quadrático - O(*n*<sup>*2*</sup>)</mark>
 ```python
1   def quadratic(n):
2       result = 0
3       for i in xrange(n):
4           for j in xrange(i, n):
5               result += 1
6       return result
 ```

O resultado da função igual a

```math
    1/2 * (n * (n + 1)) = 1/2 * n^2 + 1/2 * n
```

(a explicação esta no exercício). Quando calculamos a complexidade nós estamos interessados no termo que cresce rápido, nós não podemos omitir as constantes, mas outros termos (```math 1/2*n ``` neste caso). Portanto nós pegamos a complexidade do tempo quadratico. Algumas vezes a complexidade depende de mais variáveis (veja o exemplo abaixo)

#### <mark>3.6. Tempo linear - O(*n* + *m*)</mark>
```python
1   def linear2(n, m):
2       result = 0
3       for i in xrange(n):
4           result += i
5       for j in xrange(m):
6           result += j
7       return result
```

## Exponencial e tempo fatorial

