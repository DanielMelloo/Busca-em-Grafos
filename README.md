# Algoritmos de Busca em Grafos Direcionados

Este código implementa algoritmos de busca em profundidade (DFS) e busca em largura (BFS) em um grafo direcionado. O objetivo é encontrar o caminho entre dois vértices específicos no grafo.

## Grafo

O grafo é representado por um dicionário, onde cada chave representa um vértice e o valor associado é uma lista de vizinhos, indicando as conexões direcionadas a partir desse vértice.

## Busca em Profundidade (DFS)

A busca em profundidade explora um caminho até o fim antes de retroceder. O algoritmo percorre o grafo de forma recursiva, visitando os vizinhos não visitados de cada vértice.

## Busca em Largura (BFS)

A busca em largura explora todos os vértices vizinhos antes de avançar para o próximo nível. O algoritmo utiliza uma fila para armazenar os vértices a serem explorados, garantindo que os vizinhos sejam visitados em ordem.

## Resultados

Após a execução dos algoritmos, é exibido o caminho encontrado para cada um deles. Caso não seja encontrado nenhum caminho, uma mensagem correspondente é exibida.

## Visualização do Grafo

A função `plotar_grafo` é utilizada para visualizar o grafo com a biblioteca NetworkX e Matplotlib. O grafo é desenhado com os vértices representados por nós e as conexões entre eles representadas por arestas.

## Utilização

Para utilizar este código, siga os passos abaixo:

1. Defina o grafo que deseja utilizar, especificando os vértices e suas conexões direcionadas.

2. Defina o vértice de início e o vértice objetivo para realizar a busca.

3. Execute o programa e veja o caminho encontrado pela busca em largura e busca em profundidade, além de visualizar o grafo com os caminhos destacados.

Para especificar o vértice de início e o vértice objetivo, você pode utilizar a função `encontrar_enesimo_termo(grafo, n)`, que retorna o n-ésimo vértice do grafo. Alternativamente, você pode simplesmente utilizar a chave do vértice diretamente.

## Estrutura de Dados para Representar o Caminho Encontrado

O caminho encontrado é representado como uma lista de vértices no código fornecido. Cada elemento da lista corresponde a um vértice visitado ao percorrer o grafo. Essa abordagem permite armazenar e manipular o caminho de forma simples e eficiente.

Por exemplo, considerando o seguinte caminho encontrado: `'A' -> 'B' -> 'C' -> 'D'`. Ele é representado pela seguinte lista:

```python
caminho = ['A', 'B', 'C', 'D']
```

Nesse caso, 'A' é o vértice inicial do caminho, seguido por 'B', 'C' e finalmente 'D', que é o vértice de destino.

Ao utilizar uma lista de vértices, podemos facilmente iterar sobre o caminho, acessar cada vértice individualmente e realizar operações adicionais, se necessário. Essa estrutura de dados simples e flexível é adequada para a maioria dos casos de uso de busca em grafos.

No entanto, é importante lembrar que essa é apenas uma das possíveis estruturas de dados para representar o caminho encontrado. Dependendo das suas necessidades específicas, você pode optar por outras estruturas, como uma lista de tuplas (vértice, aresta) ou até mesmo um objeto personalizado que ofereça propriedades e métodos adicionais relacionados ao caminho.

### Requisitos

- NetworkX: Biblioteca para manipulação e visualização de grafos.
- Matplotlib: Biblioteca para plotagem de gráficos.

Certifique-se de fornecer o grafo desejado, especificando os vértices e suas conexões direcionadas. Em seguida, execute o programa para visualizar o caminho encontrado pela busca em largura e busca em profundidade, além de visualizar o grafo com os caminhos destacados.



## Funcionalidades

- Exibe o grafo
- Realiza busca em largura
- Realiza busca em profundidade
- Multiplataforma


## Documentação do script

### Função de busca em profundidade

```http
dfs(grafo, inicio, objetivo)
```

#### Retorna o caminho após realizar busca em profundidade

### Função de busca em largura

```http
bfs(grafo, inicio, objetivo)
```

#### Retorna o caminho após realizar busca em largura


#### Tabela de utilização de ambas as funções


| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `grafo` | `dict` | **Obrigatório**. O grafo que será realizado a busca |
| `inicio` | `Any` | **Obrigatório**. A chave que será o ponto de partida da Busca. |
|         |        | **Obrigatório** O tipo de entrada necessáriamente deve ser o mesmo tipo que foi especificado no grafo |
|            |            | Pode ser de qualquer tipo. |
| `objetivo` | `Any` | **Obrigatório**. A chave que será o ponto de destino da Busca. |
|            |            | **Obrigatório** O tipo de entrada necessáriamente deve ser o mesmo tipo que foi especificado no grafo |
|            |            | Pode ser de qualquer tipo. |



### Função para plotar o grafo

```http
plotar_grafo(grafo, caminho)
```

#### Parâmetros

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `grafo`     | `dict`     | **Obrigatório**. O grafo que será plotado. |
| `caminho`   | `list`     | **Obrigatório**. O caminho que será destacado no grafo. |

## Exemplo de Utilização

Aqui está um exemplo simplificado de utilização do código:

```python

# ================== #
# Definição do grafo #
# ================== #

grafo = {
    'A': ['B', 'C'],
    'B': ['C'],
    'C': ['D'],
    'D': []
}

inicio = 'A'  # Vértice de início
objetivo = 'D'  # Vértice objetivo

# ================================ #
# Execução dos algoritmos de busca #
# ================================ #

caminho_dfs = dfs(grafo, inicio, objetivo)
caminho_bfs = bfs(grafo, inicio, objetivo)

# ======================= #
# Exibição dos resultados #
# ======================= #

print('Caminho encontrado no DFS: ', caminho_dfs)
print('Caminho encontrado no BFS: ', caminho_bfs)

# ===================== #
# Visualização do grafo #
# ===================== #

plotar_grafo(grafo)

plt.show()
```

## Screenshots

<img src="https://cdn.discordapp.com/attachments/1110659107913990184/1110659303024636004/Grafo.png">

### Definição de um grafo com arestas direcionadas e não direcionadas

<img src="https://media.discordapp.net/attachments/1110659107913990184/1110659302177374308/Inicializacao.png" alt="Inicialização" style="max-width: 500px;">

### Inicialização de variáveis

<img src="https://media.discordapp.net/attachments/1110659107913990184/1110659302613602394/Plot.png" alt="Plot" style="max-width: 500px;">

### Plotando o grafo

<img src="https://cdn.discordapp.com/attachments/1110659107913990184/1110662567778603148/grafo.jpg" alt="Grafo" style="max-width: 500px;">


### Resultado do grafo

<img src="https://cdn.discordapp.com/attachments/1110659107913990184/1110663030418714654/caminho.jpg" alt="Grafo" style="max-width: 500px;">

### Caminho encontrado em DFS e BFS


## Relacionados

Segue alguns projetos relacionados

[Arvore Binária Com Algoritmo DSW](https://github.com/DanielMelloo/Arvore-Binaria-DSW)

[Filas Listas e Pilhas](https://github.com/DanielMelloo/Filas-Listas-e-Pilhas)


## Autores

- [@DanielMelloo](https://github.com/DanielMelloo)


## Feedback

Se você tiver algum feedback, por favor nos deixe saber por meio de danielmello.dev@gmail.com

