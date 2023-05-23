# ======= #
# imports #
# ======= #

import networkx as nx
import matplotlib.pyplot as plt

def dfs(grafo, inicio, objetivo):
    visitados = set()
    caminho = []
    
    def dfs_visit(vertice):
        nonlocal caminho
        visitados.add(vertice)
        caminho.append(vertice)

        if vertice == objetivo:
            return True

        for vizinho in grafo[vertice]:
            if vizinho not in visitados:
                if dfs_visit(vizinho):
                    return True

        caminho.pop()

        return False
    
    dfs_visit(inicio)
    return caminho

def bfs(grafo, inicio, objetivo):
    visitados = set()
    caminho = []
    
    fila = []
    fila.append(inicio)
    visitados.add(inicio)

    while fila:
        vertice = fila.pop(0)
        caminho.append(vertice)

        if vertice == objetivo:
            return caminho

        for vizinho in grafo[vertice]:
            if vizinho not in visitados:
                fila.append(vizinho)
                visitados.add(vizinho)

    return []

def plotar_grafo(grafo):
    G = nx.DiGraph()
    for vertice, vizinhos in grafo.items():
        G.add_edges_from([(vertice, vizinho) for vizinho in vizinhos])

    pos = nx.kamada_kawai_layout(G)  # Layout do grafo
    # pos = nx.spring_layout(G)

    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, width=0.5)  # Plotagem do grafo

    # Ajuste opcional para melhorar a aparência do grafo
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.show()
    
encontrar_enesimo_termo = lambda grafo, n: list(grafo.keys())[n]

def main():
      
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
    
    inicio = encontrar_enesimo_termo (grafo_list, 0)
    objetivo = encontrar_enesimo_termo (grafo_list, 15)
    
    caminho_dfs = dfs(grafo_list, inicio, objetivo)
    caminho_bfs = bfs(grafo_list, inicio, objetivo)

    if caminho_dfs:
        print('caminho no DFS: '+ str(caminho_dfs))
    else:
        print("Caminho não encontrado.")
    
        
    if caminho_bfs:
        print('caminho no BFS: '+ str(caminho_bfs))
    else:
        print("Caminho não encontrado.")


    plotar_grafo(grafo_list)
    
    plt.show()
    
if __name__ == "__main__":
    main()



