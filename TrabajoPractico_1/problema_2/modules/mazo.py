
# mazo.py

from modules.LDE import ListaDobleEnlazada  # Importa la clase ListaDobleEnlazada

class DequeEmptyError(Exception):
    pass  # Define una excepción personalizada para cuando el mazo está vacío

class Mazo:
    def __init__(self):
        self._cartas = ListaDobleEnlazada()  # Inicializa una lista doblemente enlazada para almacenar las cartas

    def poner_carta_arriba(self, carta):
        self._cartas.agregar_al_inicio(carta)  # Agrega una carta al inicio del mazo

    def poner_carta_abajo(self, carta):
        self._cartas.agregar_al_final(carta)  # Agrega una carta al final del mazo

    def sacar_carta_arriba(self, mostrar=False):
        if self._cartas.tamanio == 0:
            raise DequeEmptyError("El mazo está vacío")
        carta = self._cartas.cabeza.dato
        self._cartas.cabeza = self._cartas.cabeza.siguiente
        if self._cartas.cabeza is not None:
            self._cartas.cabeza.anterior = None
        else:
            self._cartas.cola = None
        self._cartas.tamanio -= 1
        if mostrar:
            print(f'Sacando carta: {carta}')
        return carta
    
    def __len__(self):
        return self._cartas.tamanio  # Devuelve el tamaño del mazo