from random import randint
import random
def ordenamiento_quicksort(lista):
   ordenamiento_quicksortAuxiliar(lista,0,len(lista)-1)

def ordenamiento_quicksortAuxiliar(lista,primero,ultimo):
   if primero<ultimo:
       puntoDivision = particion(lista,primero,ultimo)
       ordenamiento_quicksortAuxiliar(lista,primero,puntoDivision-1)
       ordenamiento_quicksortAuxiliar(lista,puntoDivision+1,ultimo)

def particion(lista,primero,ultimo):
   valorPivote = lista[primero]
   marcaIzq = primero+1
   marcaDer = ultimo
   hecho = False
   while not hecho:
       while marcaIzq <= marcaDer and lista[marcaIzq] <= valorPivote:
           marcaIzq = marcaIzq + 1
       while lista[marcaDer] >= valorPivote and marcaDer >= marcaIzq:
           marcaDer = marcaDer -1
       if marcaDer < marcaIzq:
           hecho = True
       else:
           temp = lista[marcaIzq]
           lista[marcaIzq] = lista[marcaDer]
           lista[marcaDer] = temp
   temp = lista[primero]
   lista[primero] = lista[marcaDer]
   lista[marcaDer] = temp
   return marcaDer

if __name__ == '__main__':
    # ordena numeros y palabras
    M, N = 500, 1000
    datos = [randint(M, N) for i in range(N)]
    datos = []
    for _ in range(N):
         datos.append(randint(M, N)) 
    ordenamiento_quicksort(datos)
    print(datos)