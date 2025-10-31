class Palabra:
    def __init__(self, texto):
        self.texto = texto
        self.totalAscii = self.calcular_ascii()
        self.indice_ascii = 0

    def calcular_ascii(self):
        suma = 0
        for caracter in self.texto:
            suma += ord(caracter)
        return suma

    def sumar_siguiente_ascii(self):
        if self.indice_ascii < len(self.texto):
            caracter = self.texto[self.indice_ascii]
            valor = ord(caracter)
            self.totalAscii += valor
            self.indice_ascii += 1
