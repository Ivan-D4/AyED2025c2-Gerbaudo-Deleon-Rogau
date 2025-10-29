import heapq

class ColaPrioridad:
    def __init__(self):
        self.heap = []
        self.posiciones = {}

    def construir_monticulo(self, lista):
        self.heap = lista
        heapq.heapify(self.heap)
        self._actualizar_posiciones()

    def esta_vacia(self):
        return len(self.heap) == 0

    def eliminar_min(self):
        distancia, vertice = heapq.heappop(self.heap)
        self._actualizar_posiciones()
        return vertice

    def contiene(self, vertice):
        return any(v == vertice for _, v in self.heap)

    def decrementar_clave(self, vertice, nuevo_valor):
        # Eliminar el vértice actual del heap
        self.heap = [(d, v) for d, v in self.heap if v != vertice]
        # Agregarlo con nuevo valor
        heapq.heappush(self.heap, (nuevo_valor, vertice))
        self._actualizar_posiciones()

    def _actualizar_posiciones(self):
        self.posiciones = {v: i for i, (d, v) in enumerate(self.heap)}
