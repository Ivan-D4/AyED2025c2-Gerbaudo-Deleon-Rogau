from matplotlib import pyplot as plt
from random import randint
import time
from modules.P3_Oburbuja import ordenamiento_burbuja
from modules.P3_Oquicksort import ordenamiento_quicksort
from modules.P3_Oradix import ordenamiento_radix

def medir_tiempos(metodo_ord, tamanos):
    tiempos_ord_selecc = []

    for n in tamanos:
        datos = [randint(1, 1000) for _ in range(n)]

        inicio = time.perf_counter()
        metodo_ord(datos)
        fin = time.perf_counter()
        tiempos_ord_selecc.append(fin - inicio)
        
        print(f"Tiempo de ordenamiento por seleccion para n={n}: {fin - inicio:.6f} segundos")
    
    return tiempos_ord_selecc

if __name__ == '__main__':
     tamanos = [1, 10, 100, 200, 500, 700, 1000]
     medir_tiempos(sorted,tamanos)

     def graficar_tiempos(lista_metodos_ord, k=1001, l=20):
        tamanos = [n for n in range(1, k, l)]
        plt.figure(figsize=(10, 6))
        for metodo_ord in lista_metodos_ord:
            tiempos = medir_tiempos(metodo_ord, tamanos)
            plt.plot(tamanos, tiempos, marker='o', label=metodo_ord.__name__)

        plt.xlabel('Tamaño de la lista')
        plt.ylabel('Tiempo (segundos)')
        plt.title('Comparación de tiempos de ordenamiento')
        plt.legend()
        plt.grid()
        plt.show()

if __name__ == '__main__':
   
   graficar_tiempos([ordenamiento_burbuja])
   graficar_tiempos([ordenamiento_quicksort])
   graficar_tiempos([ordenamiento_radix])
   graficar_tiempos([ordenamiento_burbuja,ordenamiento_quicksort,ordenamiento_radix])
