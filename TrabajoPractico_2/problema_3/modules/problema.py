import sys
from modules.cola_prioridad import ColaPrioridad

# -------------------- Clase Grafo --------------------
class Grafo:
    def __init__(self):
        self.listaVertices = {}
        self.numVertices = 0

    def agregarVertice(self, clave):
        self.numVertices += 1
        nuevoVertice = Vertice(clave)
        self.listaVertices[clave] = nuevoVertice
        return nuevoVertice

    def obtenerVertice(self, n):
        return self.listaVertices.get(n)

    def __contains__(self, n):
        return n in self.listaVertices

    def agregarArista(self, de, a, costo=0):
        if de not in self.listaVertices:
            self.agregarVertice(de)
        if a not in self.listaVertices:
            self.agregarVertice(a)
        self.listaVertices[de].agregarVecino(self.listaVertices[a], costo)
        self.listaVertices[a].agregarVecino(self.listaVertices[de], costo)

    def obtenerVertices(self):
        return self.listaVertices.keys()

    def __iter__(self):
        return iter(self.listaVertices.values())

# -------------------- Clase Vertice --------------------
class Vertice:
    def __init__(self, clave):
        self.id = clave
        self.conectadoA = {}
        self.distancia = sys.maxsize
        self.predecesor = None

    def __lt__(self, other):
        return self.id < other.id  # Para desempatar en heapq

    def agregarVecino(self, vecino, ponderacion=0):
        self.conectadoA[vecino] = ponderacion

    def obtenerConexiones(self):
        return self.conectadoA.keys()

    def obtenerId(self):
        return self.id

    def obtenerPonderacion(self, vecino):
        return self.conectadoA[vecino]

    def asignar_distancia(self, valor):
        self.distancia = valor

    def obtener_distancia(self):
        return self.distancia

    def asignar_predecesor(self, vertice):
        self.predecesor = vertice

    def obtener_predecesor(self):
        return self.predecesor

# -------------------- Algoritmo de Prim --------------------
def prim(G, inicio_id):
    cp = ColaPrioridad()
    for v in G:
        v.asignar_distancia(sys.maxsize)
        v.asignar_predecesor(None)

    inicio = G.obtenerVertice(inicio_id)
    inicio.asignar_distancia(0)

    cp.construir_monticulo([(v.obtener_distancia(), v) for v in G])

    while not cp.esta_vacia():
        vertice_actual = cp.eliminar_min()
        for vertice_siguiente in vertice_actual.obtenerConexiones():
            nuevo_costo = vertice_actual.obtenerPonderacion(vertice_siguiente)
            if cp.contiene(vertice_siguiente) and nuevo_costo < vertice_siguiente.obtener_distancia():
                vertice_siguiente.asignar_predecesor(vertice_actual)
                vertice_siguiente.asignar_distancia(nuevo_costo)
                cp.decrementar_clave(vertice_siguiente, nuevo_costo)

    arbol = {}
    total_distancia = 0
    for v in G:
        pred = v.obtener_predecesor()
        dist = v.obtener_distancia()
        if pred:
            arbol[v.obtenerId()] = (pred.obtenerId(), dist)
            total_distancia += dist

    return arbol, total_distancia

# -------------------- Cargar Grafo desde archivo --------------------
def cargar_grafo_desde_archivo(nombre_archivo):
    g = Grafo()
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            partes = linea.strip().split(',')
            if len(partes) == 3:
                de, a, distancia = partes[0].strip(), partes[1].strip(), int(partes[2].strip())
                g.agregarArista(de, a, distancia)
    return g

# -------------------- Mostrar Resultados ------------------
def mostrar_resultados(grafo, arbol, total_distancia):
    aldeas = sorted(grafo.obtenerVertices())
    print("📜 Lista de aldeas en orden alfabético:")
    for aldea in aldeas:
        print(f"- {aldea}")

    print("\n📡 Distribución de mensajes:")
    for aldea in aldeas:
        if aldea == "Peligros":
            vecinos = [v.obtenerId() for v in grafo.obtenerVertice(aldea).obtenerConexiones()]
            enviados = [v for v in vecinos if v in arbol]
            print(f"{aldea} envía mensaje a: {', '.join(enviados)}")
        else:
            padre, _ = arbol.get(aldea, (None, None))
            hijos = [k for k, v in arbol.items() if v[0] == aldea]
            print(f"{aldea} recibe mensaje de: {padre}")
            if hijos:
                print(f"{aldea} envía mensaje a: {', '.join(hijos)}")

    print(f"\n📦 Suma total de distancias recorridas: {total_distancia} leguas")

# -------------------- Ejecución Principal --------------------
if __name__ == "__main__":
    grafo = cargar_grafo_desde_archivo("modules/aldeas.txt")
    arbol, total_distancia = prim(grafo, "Peligros")
    mostrar_resultados(grafo, arbol, total_distancia)
