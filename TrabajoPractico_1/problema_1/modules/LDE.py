class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None


class ListaDobleEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamanio = 0

    def agregar_al_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
        self.cabeza.anterior = None
        self.tamanio += 1

    def agregar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.cola
            self.cola = nuevo_nodo
        self.tamanio += 1

    def insertar(self, dato, posicion):
        if posicion < 0 or posicion > self.tamanio:
            raise Exception("Posición inválida")
        if posicion == 0:
            self.agregar_al_inicio(dato)
        elif posicion == self.tamanio:
            self.agregar_al_final(dato)
        else:
            nuevo_nodo = Nodo(dato)
            actual = self.cabeza
            for _ in range(posicion):
                actual = actual.siguiente
            nuevo_nodo.anterior = actual.anterior
            nuevo_nodo.siguiente = actual
            actual.anterior.siguiente = nuevo_nodo
            actual.anterior = nuevo_nodo
            self.tamanio += 1

    def copiar(self):
        copia = ListaDobleEnlazada()
        actual = self.cabeza
        while actual:
            copia.agregar_al_final(actual.dato)
            actual = actual.siguiente
        return copia

    def extraer(self, posicion=None):
        if self.tamanio == 0:
            raise Exception("La lista está vacía")
        if posicion is None:
            posicion = self.tamanio - 1
        elif posicion < 0:
            posicion = self.tamanio + posicion
        if posicion < 0 or posicion >= self.tamanio:
            raise Exception("Posición inválida")

        if posicion == 0:
            nodo_extraido = self.cabeza
            self.cabeza = nodo_extraido.siguiente
            if self.cabeza:
                self.cabeza.anterior = None
            else:
                self.cola = None
        elif posicion == self.tamanio - 1:
            nodo_extraido = self.cola
            self.cola = nodo_extraido.anterior
            if self.cola:
                self.cola.siguiente = None
            else:
                self.cabeza = None
        else:
            actual = self.cabeza
            for _ in range(posicion):
                actual = actual.siguiente
            nodo_extraido = actual
            actual.anterior.siguiente = actual.siguiente
            actual.siguiente.anterior = actual.anterior

        self.tamanio -= 1
        return nodo_extraido.dato

    def invertir(self):
        actual = self.cabeza
        self.cabeza, self.cola = self.cola, self.cabeza
        while actual:
            actual.anterior, actual.siguiente = actual.siguiente, actual.anterior
            actual = actual.anterior
        if self.cabeza:
            self.cabeza.anterior = None
        if self.cola:
            self.cola.siguiente = None

    def esta_vacia(self):
        return self.tamanio == 0

    def concatenar(self, otra_lista):
        if not isinstance(otra_lista, ListaDobleEnlazada):
            raise Exception("El argumento debe ser una lista doblemente enlazada")
        if otra_lista.esta_vacia():
            return

        # Crear copia de la lista a concatenar
        lista_copia = otra_lista.copiar()

        if self.esta_vacia():
            self.cabeza = lista_copia.cabeza
            self.cola = lista_copia.cola
        else:
            self.cola.siguiente = lista_copia.cabeza
            lista_copia.cabeza.anterior = self.cola
            self.cola = lista_copia.cola
        self.tamanio += lista_copia.tamanio

    def __len__(self):
        return self.tamanio

    def __add__(self, otra_lista):
        nueva_lista = self.copiar()
        nueva_lista.concatenar(otra_lista)
        return nueva_lista

    def __iter__(self):
        actual = self.cabeza
        while actual:
            yield actual.dato
            actual = actual.siguiente
