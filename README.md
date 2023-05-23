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

<!-- 
## Screenshots

![Grafo](https://cdn.discordapp.com/attachments/1110659107913990184/1110659303024636004/Grafo.png)
![Inicialização](https://media.discordapp.net/attachments/1110659107913990184/1110659302177374308/Inicializacao.png)
![Plot](https://media.discordapp.net/attachments/1110659107913990184/1110659302613602394/Plot.png ) -->

## Screenshots

<img src="https://cdn.discordapp.com/attachments/1110659107913990184/1110659303024636004/Grafo.png" ">
<img src="https://media.discordapp.net/attachments/1110659107913990184/1110659302177374308/Inicializacao.png" alt="Inicialização" style="max-width: 500px;">
<img src="https://media.discordapp.net/attachments/1110659107913990184/1110659302613602394/Plot.png" alt="Plot" style="max-width: 500px;">

## Relacionados

Segue alguns projetos relacionados

[Awesome README](https://github.com/matiassingers/awesome-readme)


## Autores

- [@DanielMelloo](https://github.com/DanielMelloo)


## Feedback

Se você tiver algum feedback, por favor nos deixe saber por meio de danielmello.dev@gmail.com

