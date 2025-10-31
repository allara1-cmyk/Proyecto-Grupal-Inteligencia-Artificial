import matplotlib.pyplot as plt
import networkx as nx

def graficar_arbol(nodo):
    G = nx.DiGraph()
    etiquetas = {}
    def recorrer(n, padre=None):
        if n:
            G.add_node(n.palabra)
            etiquetas[n.palabra] = n.palabra
            if padre:
                G.add_edge(padre.palabra, n.palabra)
            recorrer(n.izq, n)
            recorrer(n.der, n)
    recorrer(nodo)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, labels=etiquetas, node_color='lightblue', node_size=1500)
    plt.show()

# Visualizar el árbol creado arriba
graficar_arbol(arbol.raiz)
