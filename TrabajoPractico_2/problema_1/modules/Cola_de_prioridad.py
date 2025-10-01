from Monticulo_binario import MonticuloBinario  # Asegurate de que el nombre del archivo sea correcto

class ColaDePrioridad:
    def __init__(self):
        self.monticulo = MonticuloBinario()

    def encolar(self, elemento):
        self.monticulo.insertar(elemento)

    def desencolar(self):
        return self.monticulo.eliminarMin()

    def esta_vacia(self):
        return self.monticulo.tamanoActual == 0

    def ver_minimo(self):
        if self.esta_vacia():
            return None
        return self.monticulo.listaMonticulo[1]
