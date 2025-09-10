# mazo.py

from modulo1 import ListaDobleEnlazada  # Importa la clase ListaDobleEnlazada

class DequeEmptyError(Exception):
    pass  # Define una excepción personalizada para cuando el mazo está vacío

class Mazo:
     
    def __init__(self):
        self._cartas = ListaDobleEnlazada()  # Inicializa una lista doblemente enlazada para almacenar las cartas

    def agregar_al_inicio(self, carta):
        self._cartas.agregar_al_inicio(carta)  # Agrega una carta al inicio del mazo

    def agregar_al_final(self, carta):
        self._cartas.agregar_al_final(carta)  # Agrega una carta al final del mazo

    def insertar(self, carta, posicion):
        self._cartas.insertar(carta, posicion)  # Inserta una carta en una posición específica del mazo

    def copiar(self):
        nuevo_mazo = Mazo()  # Crea un nuevo mazo
        actual = self._cartas.cabeza  # Comienza desde la cabeza de la lista
        while actual is not None:
            nuevo_mazo.agregar_al_final(actual.dato)  # Copia cada carta al nuevo mazo
            actual = actual.siguiente
        return nuevo_mazo  # Devuelve el nuevo mazo copiado

    def eliminar_del_inicio(self):
        if self.esta_vacio():
            raise DequeEmptyError("El mazo está vacío")  # Lanza una excepción si el mazo está vacío
        dato = self._cartas.cabeza.dato  # Obtiene la carta en la cabeza
        self._cartas.cabeza = self._cartas.cabeza.siguiente  # Actualiza la cabeza al siguiente nodo
        if self._cartas.cabeza is not None:
            self._cartas.cabeza.anterior = None  # Actualiza el anterior de la nueva cabeza
        else:
            self._cartas.cola = None  # Si la lista queda vacía, también actualiza la cola
        self._cartas.tamanio -= 1  # Decrementa el tamaño del mazo
        return dato  # Devuelve la carta eliminada

    def eliminar_del_final(self):
        if self.esta_vacio():
            raise DequeEmptyError("El mazo está vacío")  # Lanza una excepción si el mazo está vacío
        dato = self._cartas.cola.dato  # Obtiene la carta en la cola
        self._cartas.cola = self._cartas.cola.anterior  # Actualiza la cola al nodo anterior 
        if self._cartas.cola is not None:
            self._cartas.cola.siguiente = None  # Actualiza el siguiente de la nueva cola
        else:      
            self._cartas.cabeza = None  # Si la lista queda vacía, también actualiza la cabeza
        self._cartas.tamanio -= 1  # Decrementa el tamaño del mazo
        return dato  # Devuelve la carta eliminada
    def eliminar(self, posicion):
        if self.esta_vacio():
            raise DequeEmptyError("El mazo está vacío")  # Lanza una excepción si el mazo está vacío
        if posicion < 0 or posicion >= self._cartas.tamanio:
            raise Exception("Posición inválida")  # Lanza una excepción si la posición es inválida
        if posicion == 0:
            return self.eliminar_del_inicio()  # Elimina del inicio si la posición es 0
        elif posicion == self._cartas.tamanio - 1:  
            return self.eliminar_del_final()  # Elimina del final si la posición es la última
        else:
            actual = self._cartas.cabeza
            for _ in range(posicion):
                actual = actual.siguiente
            dato = actual.dato
            actual.anterior.siguiente = actual.siguiente  # Actualiza los enlaces para eliminar el nodo
            actual.siguiente.anterior = actual.anterior
            self._cartas.tamanio -= 1  # Decrementa el tamaño del mazo
            return dato  # Devuelve la carta eliminada
    def esta_vacio(self):
        return self._cartas.tamanio == 0  # Verifica si el mazo está vacío
    def __len__(self):
        return self._cartas.tamanio  # Devuelve el tamaño del mazo
    def __str__(self):
        cartas = []
        actual = self._cartas.cabeza
        while actual is not None:
            cartas.append(str(actual.dato))  # Convierte cada carta a cadena
            actual = actual.siguiente
        return "Mazo: [" + ", ".join(cartas) + "]"  # Devuelve una representación en cadena del mazo
    def __repr__(self):
        return str(self)
