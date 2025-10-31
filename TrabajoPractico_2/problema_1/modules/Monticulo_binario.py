
class MonticuloBinario:
    '''
    Un montículo binario permite agregar y hacer avanzar ítems en O(log n).
    En este caso utilizamos un montículo mínimo, es decir que el ítem con 
    el valor más bajo tiene la prioridad más alta.
    '''
    def __init__(self): # Inicializa el montículo
        self.listaMonticulo = [0] # Inicializa la lista con un cero para facilitar los cálculos de índices
        self.tamanoActual = 0 # Guarda el número de elementos actuales en el montículo

    def infiltArriba(self,i): # Reorganiza hacia arriba, manteniendo la propiedad de montículo mínimo 
        while i // 2 > 0: # Recorre hacia arriba mientras no llegue a la raíz
          if self.listaMonticulo[i] < self.listaMonticulo[i // 2]:# Compara el valor del nodo con su padre. Si es menor se intercambian 
             tmp = self.listaMonticulo[i // 2] # Realiza el intercambio de valores 
             self.listaMonticulo[i // 2] = self.listaMonticulo[i]
             self.listaMonticulo[i] = tmp
          i = i // 2 # Sube al padre 

    def insertar(self,k): # Inserta un nuevo elemento en el montículo
      self.listaMonticulo.append(k) # Añade el nuevo elemento al final de la lista
      self.tamanoActual = self.tamanoActual + 1 # Actualiza el tamaño del montículo 
      self.infiltArriba(self.tamanoActual) # Reorganiza el montículo para mantener la propiedad de montículo mínimo

    def infiltAbajo(self,i): #Reorganiza hacia abajo, después de eliminar el elemento mínimo
      while (i * 2) <= self.tamanoActual: # Mientras el nodo tenga al menos un hijo
          hm = self.hijoMin(i) # Obtiene el índice del hijo con el menor valor 
          if self.listaMonticulo[i] > self.listaMonticulo[hm]: # Compara el valor del nodo con su hijo menor. Si el hijo es menor, se intercambian
              tmp = self.listaMonticulo[i] # Realiza el intercambio de valores
              self.listaMonticulo[i] = self.listaMonticulo[hm]
              self.listaMonticulo[hm] = tmp
          i = hm # Baja al hijo menor para seguir comparando

    def hijoMin(self,i): # Determina cúal de los hijos de un nodo es el de menor valor 
      if i * 2 + 1 > self.tamanoActual: # Si no tiene hijo derecho, devuelve el izquierdo
          return i * 2
      else: # Si tiene ambos hijos, compara sus valores
          if self.listaMonticulo[i*2] < self.listaMonticulo[i*2+1]: # Compara
              return i * 2 # Devuelve el índice del hijo izquierdo
          else:
              return i * 2 + 1 # Devuelve el índice del hijo derecho

    def eliminarMin(self): # Elimina y devuelve el elemento de menor valor (la raíz del montículo)
      valorSacado = self.listaMonticulo[1] # Guarda el valor de minimo qu está en la raíz
      self.listaMonticulo[1] = self.listaMonticulo[self.tamanoActual] # Reemplaza la raíz con el último elemento del montículo
      self.tamanoActual = self.tamanoActual - 1 # Actualiza el tamaño del montículo 
      self.listaMonticulo.pop() # Elimina el último elemento de la lista (fue movido a la raíz)
      self.infiltAbajo(1) # Reorganiza el montículo para mantener la propiedad de montículo mínimo
      return valorSacado 

    def construirMonticulo(self,unaLista): # Construye un montículo a partir de una lista dada
      i = len(unaLista) // 2 # Empieza desde el último nodo padre 
      self.tamanoActual = len(unaLista) # Actualiza el tamaño del montículo
      self.listaMonticulo = [0] + unaLista[:] # Inicializa la lista del montículo con un cero, seguido de los elementos de la lista
      while (i > 0): # Recorre hacia atrás desde el último padre hasta la raíz
          self.infiltAbajo(i) # Organiza hacia abajo desde el nodo actual
          i = i - 1

#miMonticulo = MonticuloBinario()
#miMonticulo.construirMonticulo(salita.cola_de_espera)
