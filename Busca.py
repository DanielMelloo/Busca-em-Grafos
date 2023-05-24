

# ======= #
# imports #
# ======= #


import networkx as nx
import matplotlib.pyplot as plt


# ======= #
# Funções #
# ======= #

def dfs(grafo, inicio, objetivo):
    # Função de busca em profundidade (DFS)
    visitados = set()  # Conjunto de vértices visitados
    caminho = []  # Caminho percorrido

    def dfs(vertice):
        nonlocal caminho  # Acesso à variável caminho da função externa

        visitados.add(vertice)  # Marca o vértice como visitado
        caminho.append(vertice)  # Adiciona o vértice ao caminho

        if vertice == objetivo:  # Verifica se o vértice atual é o objetivo
            return True

        for vizinho in grafo[vertice]:  # Percorre os vizinhos do vértice atual
            if vizinho not in visitados:  # Verifica se o vizinho ainda não foi visitado
                if dfs(vizinho):  # Chamada recursiva da função DFS para o vizinho
                    return True

        caminho.pop()  # Remove o vértice atual do caminho (backtracking)

        return False

    dfs(inicio)  # Chamada inicial da função DFS

    return caminho  # Retorna o caminho percorrido


def bfs(grafo, inicio, objetivo):
    # Função de busca em largura (BFS)
    visitados = set()  # Conjunto de vértices visitados
    caminho = []  # Caminho percorrido

    fila = []  # Fila para armazenar os vértices a serem visitados
    fila.append(inicio)  # Adiciona o vértice inicial na fila
    visitados.add(inicio)  # Marca o vértice inicial como visitado

    while fila:  # Enquanto a fila não estiver vazia
        vertice = fila.pop(0)  # Remove o vértice mais antigo da fila
        caminho.append(vertice)  # Adiciona o vértice ao caminho percorrido

        if vertice == objetivo:  # Verifica se o vértice atual é o objetivo
            return caminho

        for vizinho in grafo[vertice]:  # Percorre os vizinhos do vértice atual
            if vizinho not in visitados:  # Verifica se o vizinho ainda não foi visitado
                fila.append(vizinho)  # Adiciona o vizinho na fila
                visitados.add(vizinho)  # Marca o vizinho como visitado

    return []  # Retorna uma lista vazia se o caminho não for encontrado


def plotar_grafo(grafo):
    # Função para plotar o grafo
    G = nx.DiGraph()
    for vertice, vizinhos in grafo.items():
        G.add_edges_from([(vertice, vizinho) for vizinho in vizinhos])

    pos = nx.kamada_kawai_layout(G)  # Layout do grafo
    # pos = nx.spring_layout(G)

    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, width=0.5)  # Plotagem do grafo


    # ====================== #
    # Ajuste Visual do Grafo #
    # ====================== #

    # Obtém os atributos das arestas do grafo
    edge_labels = nx.get_edge_attributes(G, 'weight')

    # Adiciona legendas nas arestas do grafo
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.show()


encontrar_enesimo_termo = lambda grafo, n: list(grafo.keys())[n]  # Função para encontrar o n-ésimo termo do grafo


def main():
    # Função principal do programa
    
    # ====================== #
    # Definição de variáveis #
    # ====================== #

    grafo = {
        0: [1],
        1: [0, 2, 3],
        2: [0, 1],
        3: [1, 4, 5],
        4: [0, 3],
        5: [3, 6, 9],
        6: [5, 7, 10],
        7: [6, 8],
        8: [7],
        9: [5],
        10: [3, 11, 12],
        11: [5, 10, 13],
        12: [10, 13, 15],
        13: [11, 12],
        14: [15, 16],
        15: [14, 16],
        16: [14, 15]
    }

    grafo_list = {
        'o125': ['o123'],
        'o123': ['o125', 'r123', 'o119'],
        'r123': ['o125', 'o123'],
        'o119': ['o123', 'Almoxarifado', 'o109'],
        'Almoxarifado': ['o125', 'o119'],
        'o109': ['o119', 'o103', 'o111'],
        'o103': ['o109', 'ts', 'b3'],
        'ts': ['o103', 'Correio'],
        'Correio': ['ts'],
        'o111': ['o109'],
        'b3': ['o119', 'b4', 'b4'],
        'b4': ['o109', 'b3', 'b2'],
        'b4': ['b3', 'b2', 'c2'],
        'b2': ['b4', 'b4'],
        'c3': ['c2', 'c1'],
        'c2': ['c3', 'c1'],
        'c1': ['c3', 'c2']
    }

    grafo2 = {
        1: [2, 3],
        2: [3, 4],
        3: [4],
        4: [1]
    }


    
    inicio = encontrar_enesimo_termo(grafo_list, 0)  # Encontra o vértice inicial
    objetivo = encontrar_enesimo_termo(grafo_list, 15)  # Encontra o vértice objetivo
    objetivo = 'Correio'  # Define o vértice objetivo

    # =========================== #
    # Chamada de Funções de Busca #
    # =========================== #
    
    caminho = dfs(grafo_list, inicio, objetivo)  # Realiza a busca em profundidade
    caminho2 = bfs(grafo_list, inicio, objetivo)  # Realiza a busca em largura

    # ================ #
    # Exibir Resultado #
    # ================ #

    if caminho:
        print('Caminho no DFS: ' + str(caminho))  # Imprime o caminho encontrado no DFS
        print('Caminho no BFS: ' + str(caminho2))  # Imprime o caminho encontrado no BFS
    else:
        print("Caminho não encontrado.")

    plotar_grafo(grafo_list)  # Plota o grafo

    plt.show()  # Exibe o gráfico


if __name__ == "__main__":
    main()
