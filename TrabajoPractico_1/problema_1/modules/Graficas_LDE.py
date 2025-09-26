from matplotlib import pyplot as plt
from random import randint
import time
from modules.LDE import ListaDobleEnlazada

def medir_tiempos_len(tamanos):
    tiempos = []
    for n in tamanos:
        lista = ListaDobleEnlazada()
        for _ in range(n):
            lista.agregar_al_final(randint(1, 1000))
        inicio = time.perf_counter()
        _ = len(lista)
        fin = time.perf_counter()
        tiempos.append(fin - inicio)
    return tiempos

def medir_tiempos_copia(tamanos):
    tiempos = []
    for n in tamanos:
        lista = ListaDobleEnlazada()
        for _ in range(n):
            lista.agregar_al_final(randint(1, 1000))
        inicio = time.perf_counter()
        copia = lista.copiar()
        fin = time.perf_counter()
        tiempos.append(fin - inicio)
    return tiempos

def medir_tiempos_invertir(tamanos):
    tiempos = []
    for n in tamanos:
        lista = ListaDobleEnlazada()
        for _ in range(n):
            lista.agregar_al_final(randint(1, 1000))
        inicio = time.perf_counter()
        lista.invertir()
        fin = time.perf_counter()
        tiempos.append(fin - inicio)
    return tiempos

def graficar_tiempos():
    tamanos = [n for n in range(1, 1001, 20)]
    tiempos_len = medir_tiempos_len(tamanos)
    tiempos_copia = medir_tiempos_copia(tamanos)
    tiempos_invertir = medir_tiempos_invertir(tamanos)

    plt.figure(figsize=(10, 6))
    plt.plot(tamanos, tiempos_len, marker='o', label="len (O(1))")
    plt.plot(tamanos, tiempos_copia, marker='o', label="copiar (O(n))")
    plt.plot(tamanos, tiempos_invertir, marker='o', label="invertir (O(n))")
    plt.xlabel('Tamaño de la lista')
    plt.ylabel('Tiempo (segundos)')
    plt.title('Tiempos de ejecución: len, copiar e invertir en ListaDobleEnlazada')
    plt.grid()
    plt.legend()
    plt.show()
    

if __name__ == '__main__':
    graficar_tiempos()