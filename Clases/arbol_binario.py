from Clases.nodo import Nodo

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, palabra, significado):
        nuevo = Nodo(palabra, significado)
        if self.raiz is None:
            self.raiz = nuevo
        else:
            self._insertar_rec(self.raiz, nuevo)

    def _insertar_rec(self, actual, nuevo):
        while nuevo.totalAscii == actual.totalAscii:
            nuevo.sumar_siguiente_ascii()
        if nuevo.totalAscii < actual.totalAscii:
            if actual.izq is None:
                actual.izq = nuevo
            else:
                self._insertar_rec(actual.izq, nuevo)
        else:
            if actual.der is None:
                actual.der = nuevo
            else:
                self._insertar_rec(actual.der, nuevo)

    def imprimir_inorder(self):
        self._inorder(self.raiz)

    def _inorder(self, nodo):
        if nodo:
            self._inorder(nodo.izq)
            print(f"{nodo.palabra}: {nodo.significado}")
            self._inorder(nodo.der)

    def imprimir_ascii(self):
        self._imprimir_ascii_rec(self.raiz)

    def _imprimir_ascii_rec(self, nodo):
        if nodo:
            self._imprimir_ascii_rec(nodo.izq)
            print(f"{nodo.palabra} = {nodo.totalAscii}")
            self._imprimir_ascii_rec(nodo.der)
