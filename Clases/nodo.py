class Nodo:
    def __init__(self, palabra, significado):
        self.palabra = palabra
        self.significado = significado
        self.izq = None
        self.der = None
        self.totalAscii = self.calcular_ascii()
        self.indice_ascii = 0

    def calcular_ascii(self):
        suma = 0
        for caracter in self.palabra:
            suma += ord(caracter)
        return suma

    def sumar_siguiente_ascii(self):
        if self.indice_ascii < len(self.palabra):
            caracter = self.palabra[self.indice_ascii]
            valor = ord(caracter)
            self.totalAscii += valor
            self.indice_ascii += 1
