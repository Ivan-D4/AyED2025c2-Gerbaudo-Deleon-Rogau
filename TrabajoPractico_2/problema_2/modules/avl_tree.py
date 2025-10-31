from datetime import datetime # Importa el módulo datetime para manejar fechas

class Node: # Nodo del árbol AVL
    def __init__(self, key, value): # Inicializa un nodo con clave, valor, hijos y altura
        self.key = key 
        self.value = value
        self.left = None
        self.right = None
        self.height = 1
class AVLTree: # Árbol AVL
    @staticmethod 
    def _convert_date(date_str):
        """Convierte una fecha en formato string 'dd/mm/yyyy' a un objeto datetime"""
        return datetime.strptime(date_str, '%d/%m/%Y')

    @staticmethod
    def _compare_dates(date1_str, date2_str):
        """Compara dos fechas en formato string"""
        date1 = AVLTree._convert_date(date1_str)
        date2 = AVLTree._convert_date(date2_str)
        if date1 < date2:
            return -1
        elif date1 > date2:
            return 1
        return 0

    def get_records_in_range(self, fecha1, fecha2):
        """
        Devuelve una lista de tuplas (fecha, temperatura) para todas las fechas en el rango [fecha1, fecha2], ordenadas por fecha.
        """
        result = []
        self._inorder_range(self.root, fecha1, fecha2, result)
        return sorted(result, key=lambda x: self._convert_date(x[0]))

    def _inorder_range(self, node, fecha1, fecha2, result):
        """Recorre el árbol en orden y recolecta los registros en el rango [fecha1, fecha2]"""
        if not node:
            return
            
        # Si la fecha actual es mayor que fecha1, exploramos el subárbol izquierdo
        if self._compare_dates(fecha1, node.key) < 0:
            self._inorder_range(node.left, fecha1, fecha2, result)
            
        # Si la fecha actual está en el rango [fecha1, fecha2], la agregamos
        if (self._compare_dates(fecha1, node.key) <= 0 and 
            self._compare_dates(node.key, fecha2) <= 0):
            result.append((node.key, node.value))
            
        # Si la fecha actual es menor que fecha2, exploramos el subárbol derecho
        if self._compare_dates(node.key, fecha2) < 0:
            self._inorder_range(node.right, fecha1, fecha2, result)

    def __init__(self):
        self.root = None

    # Métodos públicos
    def insert(self, key, value):
        self.root = self._insert(self.root, key, value)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def search(self, key):
        node = self._search(self.root, key)
        return node.value if node else None

    def max_in_range(self, fecha1, fecha2):
        """Encuentra la temperatura máxima en un rango de fechas"""
        result = []
        self._inorder_range(self.root, fecha1, fecha2, result)
        return max(result, key=lambda x: x[1])[1] if result else None

    def min_in_range(self, fecha1, fecha2):
        """Encuentra la temperatura mínima en un rango de fechas"""
        result = []
        self._inorder_range(self.root, fecha1, fecha2, result)
        return min(result, key=lambda x: x[1])[1] if result else None

    def extreme_in_range(self, fecha1, fecha2):
        """Encuentra las temperaturas mínima y máxima en un rango de fechas"""
        result = []
        self._inorder_range(self.root, fecha1, fecha2, result)
        if not result:
            return None, None
        min_temp = min(result, key=lambda x: x[1])[1]
        max_temp = max(result, key=lambda x: x[1])[1]
        return min_temp, max_temp

    # Métodos internos recursivos
    def _insert(self, root, key, value): # Inserta un nodo y mantiene el equilibrio del árbol
        if not root:
            return Node(key, value)
        elif key < root.key:
            root.left = self._insert(root.left, key, value)
        elif key > root.key:
            root.right = self._insert(root.right, key, value)
        else:
            root.value = value  # Actualiza el valor si la clave ya existe
            return root

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        if balance > 1 and key < root.left.key: 
            return self.right_rotate(root)
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def _delete(self, root, key): # Elimina un nodo y mantiene el equilibrio del árbol
        if not root:
            return root
        elif key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = self.get_min_value_node(root.right)
            root.key, root.value = temp.key, temp.value
            root.right = self._delete(root.right, temp.key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def _search(self, root, key): # Busca un nodo por clave
        if not root or root.key == key:
            return root
        if key < root.key:
            return self._search(root.left, key)
        return self._search(root.right, key)

    def get_height(self, root): # Obtiene la altura de un nodo
        if not root:
            return 0
        return root.height

    def get_balance(self, root): # Obtiene el factor de equilibrio de un nodo
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def left_rotate(self, z): # Realiza una rotación izquierda
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def right_rotate(self, z): # Realiza una rotación derecha
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def get_min_value_node(self, root): # Obtiene el nodo con el valor mínimo en un subárbol
        if root is None or root.left is None:
            return root
        return self.get_min_value_node(root.left)