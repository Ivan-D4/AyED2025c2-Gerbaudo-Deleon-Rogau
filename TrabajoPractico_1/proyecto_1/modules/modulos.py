# módulo para organizar funciones o clases utilizadas en nuestro proyecto
# Crear tantos módulos como sea necesario para organizar el código

class nodo:
    #Define dato como nodo
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None
#Crea la lista
class listaDobleEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamanio = 0

def agregar_al_inicio(self,dato):
    # Crea un nuevo nodo
    nuevo_nodo = nodo(dato)
    if self.cabeza is None:
       self.cabeza = nuevo_nodo # Crea la cabeza
       self.cola = nuevo_nodo # Crea la cola
    else: # Si la lista no está vacía
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza.anterior = nuevo_nodo # Establece el anterior de la cabeza
        self.cabeza = nuevo_nodo # Actualiza la cabeza
    self.tamanio += 1

    def agregar_al_final(self,dato):
     nuevo_nodo = nodo(dato)
     if self.cabeza is None: # Si la lista está vacía
       self.cabeza = nuevo_nodo 
       self.cola = nuevo_nodo 
     else: 
        nuevo_nodo.anterior = self.cola # Establece el anterior de nuevo_nodo
        self.cola.siguiente = nuevo_nodo # Establece el siguiente de la cola
        self.cola = nuevo_nodo # Actualiza la cola
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
    
    def copiar(self):
        copia = listaDobleEnlazada()
        actual = self.cabeza
        while actual is not None:
            copia.agregar_al_final(actual.dato)
            actual = actual.siguiente
        return copia

    def extraer(self, posicion=None):
        if self.tamanio == 0:
            raise Exception("La lista está vacía")
        if posicion is None:
            posicion = self.tamanio - 1
        if posicion < 0 or posicion >= self.tamanio:
            raise Exception("Posición inválida")
        # Extraer de la cabeza
        if posicion == 0:
            nodo_extraido = self.cabeza
            self.cabeza = nodo_extraido.siguiente
            if self.cabeza:
                self.cabeza.anterior = None
            else:
                self.cola = None
        # Extraer de la cola
        elif posicion == self.tamanio - 1:
            nodo_extraido = self.cola
            self.cola = nodo_extraido.anterior
            if self.cola:
                self.cola.siguiente = None
            else:
                self.cabeza = None
        # Extraer de posición intermedia
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
        self.cabeza = self.cola
        self.cola = actual
        while actual is not None:
            actual.anterior, actual.siguiente = actual.siguiente, actual.anterior
            actual = actual.siguiente
        self.cola.anterior = None

    def esta_vacia(self):
        if self.tamanio == 0:
            return True
        return False

    def concatenar(self, otra_lista):
        if not isinstance(otra_lista, listaDobleEnlazada):
            raise Exception("El argumento debe ser una lista doblemente enlazada")

        if otra_lista.esta_vacia():
            return

        if self.esta_vacia():
            self.cabeza = otra_lista.cabeza
            self.cola = otra_lista.cola
        else:
            self.cola.siguiente = otra_lista.cabeza
            otra_lista.cabeza.anterior = self.cola
            self.cola = otra_lista.cola

        self.tamanio += otra_lista.tamanio

    def _len_(self):
        return self.tamanio

    def _add_(self, otra_lista):
        nueva_lista = self.copiar()
        nueva_lista.concatenar(otra_lista)
        return nueva_lista

    def _iter_(self):
        actual = self.cabeza
        for _ in range(self.tamanio):
            yield actual.dato
            actual = actual.siguiente