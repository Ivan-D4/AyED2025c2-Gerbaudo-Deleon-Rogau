class NodoArbol:
    def __init__(self, clave, valor, izquierdo=None, derecho=None, padre=None):
        self.clave = clave
        self.cargaUtil = valor
        self.hijoIzquierdo = izquierdo
        self.hijoDerecho = derecho
        self.padre = padre
        self.factorEquilibrio = 0

    def tieneHijoIzquierdo(self):
        return self.hijoIzquierdo is not None

    def tieneHijoDerecho(self):
        return self.hijoDerecho is not None

    def esHijoIzquierdo(self):
        return self.padre and self.padre.hijoIzquierdo == self

    def esHijoDerecho(self):
        return self.padre and self.padre.hijoDerecho == self

    def esRaiz(self):
        return self.padre is None

    def esHoja(self):
        return not (self.hijoIzquierdo or self.hijoDerecho)

    def tieneAlgunHijo(self):
        return self.hijoIzquierdo or self.hijoDerecho

    def tieneAmbosHijos(self):
        return self.hijoIzquierdo and self.hijoDerecho

    def reemplazarDatoDeNodo(self, clave, valor, hizq, hder):
        self.clave = clave
        self.cargaUtil = valor
        self.hijoIzquierdo = hizq
        self.hijoDerecho = hder
        if self.tieneHijoIzquierdo():
            self.hijoIzquierdo.padre = self
        if self.tieneHijoDerecho():
            self.hijoDerecho.padre = self

    def encontrarMin(self):
        actual = self
        while actual.tieneHijoIzquierdo():
            actual = actual.hijoIzquierdo
        return actual

    def encontrarSucesor(self):
        if self.tieneHijoDerecho():
            return self.hijoDerecho.encontrarMin()
        actual = self
        while actual.padre and actual.esHijoDerecho():
            actual = actual.padre
        return actual.padre

    def empalmar(self):
        if self.esHoja():
            if self.esHijoIzquierdo():
                self.padre.hijoIzquierdo = None
            else:
                self.padre.hijoDerecho = None
        elif self.tieneAlgunHijo():
            if self.tieneHijoIzquierdo():
                if self.esHijoIzquierdo():
                    self.padre.hijoIzquierdo = self.hijoIzquierdo
                else:
                    self.padre.hijoDerecho = self.hijoIzquierdo
                self.hijoIzquierdo.padre = self.padre
            else:
                if self.esHijoIzquierdo():
                    self.padre.hijoIzquierdo = self.hijoDerecho
                else:
                    self.padre.hijoDerecho = self.hijoDerecho
                self.hijoDerecho.padre = self.padre

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None
        self.tamano = 0

    def agregar(self, clave, valor):
        if self.raiz:
            self._agregar(clave, valor, self.raiz)
        else:
            self.raiz = NodoArbol(clave, valor)
        self.tamano += 1

    def _agregar(self, clave, valor, nodoActual):
        if clave < nodoActual.clave:
            if nodoActual.tieneHijoIzquierdo():
                self._agregar(clave, valor, nodoActual.hijoIzquierdo)
            else:
                nodoActual.hijoIzquierdo = NodoArbol(clave, valor, padre=nodoActual)
        else:
            if nodoActual.tieneHijoDerecho():
                self._agregar(clave, valor, nodoActual.hijoDerecho)
            else:
                nodoActual.hijoDerecho = NodoArbol(clave, valor, padre=nodoActual)
        # Aquí podrías agregar lógica de balanceo si querés que sea AVL

    def obtener(self, clave):
        return self._obtener(clave, self.raiz)

    def _obtener(self, clave, nodoActual):
        if not nodoActual:
            return None
        elif clave == nodoActual.clave:
            return nodoActual.cargaUtil
        elif clave < nodoActual.clave:
            return self._obtener(clave, nodoActual.hijoIzquierdo)
        else:
            return self._obtener(clave, nodoActual.hijoDerecho)

    def recorrido_inorder(self, nodo=None):
        if nodo is None:
            nodo = self.raiz
        if nodo:
            self.recorrido_inorder(nodo.hijoIzquierdo)
            print(f"{nodo.clave}: {nodo.cargaUtil}")
            self.recorrido_inorder(nodo.hijoDerecho)

    def max_in_range(self, fecha1, fecha2):
        return self._max_in_range(self.raiz, fecha1, fecha2)

    def _max_in_range(self, nodo, fecha1, fecha2):
        if nodo is None:
            return float('-inf')
        max_val = float('-inf')
        if fecha1 <= nodo.clave <= fecha2:
            max_val = nodo.cargaUtil
        left_max = self._max_in_range(nodo.hijoIzquierdo, fecha1, fecha2)
        right_max = self._max_in_range(nodo.hijoDerecho, fecha1, fecha2)
        return max(max_val, left_max, right_max)
    def recorrido_inorder(self, nodo=None):
       if nodo is None:
        nodo = self.raiz
       if nodo:
           self.recorrido_inorder(nodo.hijoIzquierdo)
           print(f"{nodo.clave}: {nodo.cargaUtil}")
           self.recorrido_inorder(nodo.hijoDerecho)

    
    
if __name__ == "__main__":
    arbol = ArbolBinarioBusqueda()

    # Simulamos fechas como enteros (por ejemplo, YYYYMMDD)
    arbol.agregar(20250101, 30)
    arbol.agregar(20250102, 32)
    arbol.agregar(20250103, 28)
    arbol.agregar(20250104, 35)
    arbol.agregar(20250105, 31)

    print("Recorrido del árbol:")
    arbol.recorrido_inorder()

    print("\nTemperatura máxima entre 20250102 y 20250104:")
    print(arbol.max_in_range(20250102, 20250104))  # Debería devolver 35

