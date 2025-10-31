from Monticulo_binario import MonticuloBinario  # Importa el montículo desde su archivo correspondiente

class ColaDePrioridad: #Crea la clase Cola de prioridad 
    # La cola de prioridad ingresa un elemento por el final, evalúa su prioridad y lo 
    #ubica en determinada posición, según el criterio anterior. Por cada elemento 
    #que ingresa por el final, otro elemento es removido desde el frente de la cola.
    
    def __init__(self): #Inicializa la cola de prioridad, anexandole un montículo binario
        self.monticulo = MonticuloBinario()

    def encolar(self, elemento): #Añade un elemento al montículo, para que este lo ubique según su prioridad
        self.monticulo.insertar(elemento)

    def desencolar(self): #Extrae del montículo el elemnto de menor valor, en este caso el de mayor prioridad
        return self.monticulo.eliminarMin()

    def esta_vacia(self): #Evalúa si el montículo tiene elementos o no
        return self.monticulo.tamanoActual == 0

    def ver_minimo(self): #muestra el elémento de menor prioridad
        if self.esta_vacia(): #Si no hay elementos en el montículo devuelve none 
            return None
        return self.monticulo.listaMonticulo[1] #muestra el elemento en el indice 1(el de mayor prioridad)
