class Cola:
    def __init__(self):
        self.items = []
    def encolar(self, elemento):
        self.items.append(elemento)
    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)
    def esta_vacia(self):
        return len(self.items) == 0
