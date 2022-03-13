# Array (Matriz)

Array é uma estrutura de dados que pode ser usada para armazenar muitos tipos em um só lugar. Imagine que nós tenhamos uma lista de itens: por exemplo, uma lista de shopping. Nós não mantemos todos os produtos separados por página; nós simplismente listamo-os todos juntos numa única página. Tal como uma página é conceitualmente parecida com um array. Similarmente, se o seu plano é gravar temperaturas do ar sobre os próximos 365 dias, nós não criariamos um monte de variáveis individuais, mas em vez disso, armazenariamos todos os dados em um único array.

## 2.1. Criando um array

Nós queremos criar uma lista de shopping contendo 3 produtos. Tal lista pode ser criada como se segue:

```python
shopping = ['bread', 'butter', 'cheese']
```

(sendo que: *shopping* é o nome do array e cada produto dentro é separado por vírgula). Cada item no array é chamado de elemento. Arrays podem aramazenar qualquer quantidade de elementos (assumindo que há memória suficiente). Note que a lista pode também ser vazia.

```python
shopping = []
```

Se o planejamento é gravar temperaturas do ar sobre os próximos 365 dias, nós podemos criar de antemão um lugar para armazenar os dados. O array pode ser criado da seguinte maneira.

```python
temperatures = [0] * 365
```
(isto é, nós criamos um array contendo 365 zeros).

## 2.1. Acessando valores de um array

Array provê facil acesso a todos os elementos. Dentro do array, cada elemento é atribuido a um número chamado de índice. Numeros índices são inteiros consecutivos inciados por 0. Por exemplo, no array *shopping* = ['bread', 'butter', 'cheese'], *bread* esta no índice 0, *butter* esta no índice 1 e *cheese* esta no índex 2. Se nós queremos checar qual o valor as some index (por exemplo, no índice 1), nós podemos acessar especificando o índice dentro de colchetes, exemplo: *shopping[1]*

## 2.3. Modificando valores do array

Nós podemos alterar os elementos do array como se fossem variáveis separadas, no qual cada elemento do array pode ser atribuído a um novo valor independentemente. Por exemplo, vamos dizer que nós queremos gravar que o 42º dia de medição, a temperatura do ar foi 25 graus. Isto pode ser feito com uma simples atribuição.

```python
temperatures[42] = 25
```

Se existir um produto a mais para adicionar a nossa lista do shopping, pode ser adicionado como se segue:

```python
shopping += ['eggs']
```

O índice para o elemento será o próximo inteiro depois do último (neste caso, 3)

## 2.4. Interando sobre um array

Frequentemente nós precisamos interar sobre todos os elementos do array; talvez para contar o número de itens específicos, por exemplo. Sabendo disso que o array contem *N* elementos, nós podemos interar sobre os inteiros consecutivos do índice 0 para o índice *N* - 1 e checar cada índice. O tamanho de um array pode ser encontrado usando a função *len()*. Por exemplo, contando o número de itens na lista do shopping pode ser feita rapidamente como se segue:

```python
N = len(shopping)
```

Vamos escrever uma função que conta o número de dias com temperatura negativa do ar.

#### <mark>2.1: Temperatura negative do ar</mark>
```python
1 def negative(temperatures):
2     N = len(temperatures)
3     days = 0
4     for i in xrange(N):
5         if temperatures[i] < 0:
6             days += 1
7     return days
 ```

Ao invés de interar sobre os índices, nós podemos interar sobre os elementos do array. Para fazer isso, nós podemos simplismente escrever:

```python
1 for item in array:
2     ...
 ```

Por exemplo, a solução acima pode ser simplicada como se segue:

#### <mark>2.2: Temperatura negative do ar - simplificado</mark>
```python
1 def negative(temperatures):
2     days = 0
3    for t in temperatures:
4         if t < 0:
5             days += 1
6     return days
 ```

Na solução acima, para cada temperatura, nós acrescentamos o numero de dias com a temperatura negativa se o numero for menor que 0.

## 2.5. Operações basicas no array

Existem algumas operações básicas em arrays que são muito úteis. Além da operação de comprimento:

```python
1 len([1, 2, 3]) == 3
```

e de repetição:

```python
1 ['Hello'] * 3 == ['Hello', 'Hello', 'Hello']
```

que nós já vimos, há também a concatenação:

```python
1 [1, 2, 3] + [4, 5, 6] == [1, 2, 3, 4, 5, 6]
```

que merge 2 listas, e a operação de adesão:

```python
1 'butter' in ['bread', 'butter', 'cheese'] == True
```

que verifica para a presença de um item em particular no array.

## 2.6. Exercício

**Problema:** Dado um array *A* consistindo de *N* inteiros, retorne o array invertido.
**Solução:** Nós podemos interar sobre a primeira metade do array e trocar os elementos com os da segunda parte do array.

#### <mark>2.3: Invertendo um array</mark>
```python
1 def reverse(A):
2     N = len(A)
3     for i in xrange(N // 2):
4         k = N - i - 1
5         A[i], A[k] = A[k], A[i]
6     return A
 ```

Python é uma linguagem muito rica e fornece muitas funções e métodos integrados. Acontece que já existe um método reverso embutido, que resolve este exercício. Usando tal método, o array A pode ser revertido simplesmente por:

 ```python
1 A.reverse()
```