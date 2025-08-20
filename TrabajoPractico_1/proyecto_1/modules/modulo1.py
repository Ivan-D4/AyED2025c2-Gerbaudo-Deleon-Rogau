# módulo para organizar funciones o clases utilizadas en nuestro proyecto
# Crear tantos módulos como sea necesario para organizar el código
class nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class listaDobleEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamanio = 0

def agregar_al_inicio(self,dato):
    nuevo_nodo = nodo(dato)
    if self.cabeza is None:
       self.cabeza = nuevo_nodo
       self.cola = nuevo_nodo
    else:
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza.anterior = nuevo_nodo
        self.cabeza = nuevo_nodo
    self.tamanio += 1

    def agregar_al_final(self,dato):
     nuevo_nodo = nodo(dato)
     if self.cabeza is None:
       self.cabeza = nuevo_nodo
       self.cola = nuevo_nodo
     else:
        nuevo_nodo.siguiente = self.cola
        self.cola.anterior = nuevo_nodo
        self.cola = nuevo_nodo
    self.tamanio += 1


    def insertar(self,dato,posicion):
        if posicion < 0 or posicion > self.tamanio:
            raise Exception("Posición inválida")
        if posicion == 0:
            self.agregar_al_inicio(dato)
        elif posicion == self.tamanio:
            self.agregar_al_final(dato)
        else:
            nuevo_nodo = nodo(dato)
            actual = self.cabeza
            for _ in range(posicion):
                actual = actual.siguiente

            nuevo_nodo.anterior = actual.anterior
            nuevo_nodo.siguiente = actual
            actual.anterior.siguiente = nuevo_nodo
            actual.anterior = nuevo_nodo
            self.tamanio += 1











