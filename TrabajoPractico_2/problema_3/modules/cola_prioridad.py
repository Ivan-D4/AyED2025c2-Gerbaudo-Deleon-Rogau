from .monticulo import MonticuloBinario  # Importa el montículo desde su archivo correspondiente

class ColaPrioridad:
    def __init__(self):
        self.monticulo = MonticuloBinario()
        self.elementos = {}  # Diccionario auxiliar para acceso rápido a vértices

    def construir_monticulo(self, lista):# Construye el montículo a partir de una lista de tuplas (distancia, vertice).
        self.monticulo.construirMonticulo(lista)
        # Guardamos referencias para poder verificar pertenencia y actualizar claves
        self.elementos = {v: d for d, v in lista}

    def eliminar_min(self): #Elimina y devuelve el vértice con menor distancia.
        distancia, vertice = self.monticulo.eliminarMin()
        self.elementos.pop(vertice, None)
        return vertice

    def contiene(self, vertice):#Verifica si un vértice está en la cola de prioridad.
        return vertice in self.elementos
    
    def decrementar_clave(self, vertice, nueva_distancia):#Actualiza la prioridad (distancia) de un vértice en el montículo.
       # Reconstruimos el montículo con la nueva distancia
        self.elementos[vertice] = nueva_distancia
        lista_actualizada = [(d, v) for v, d in self.elementos.items()]
        self.monticulo.construirMonticulo(lista_actualizada)

    def esta_vacia(self):
        return self.monticulo.tamanoActual == 0