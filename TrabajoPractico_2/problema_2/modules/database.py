from avl_tree import AVLTree # Importa la clase AVLTree desde el módulo avl_tree
class Temperaturas_DB: # Clase para manejar la base de datos de temperaturas
    def __init__(self): # Inicializa la base de datos con un árbol AVL vacío y contador de muestras
        self.avl_tree = AVLTree()
        self.sample_count = 0

    def guardar_temperatura(self, temperatura, fecha): # Guarda una temperatura con su fecha en el árbol
        self.avl_tree.insert(fecha, temperatura)
        self.sample_count += 1

    def devolver_temperatura(self, fecha): # Devuelve la temperatura para una fecha dada
        return self.avl_tree.search(fecha)

    def max_temp_rango(self, fecha1, fecha2): # Devuelve la temperatura máxima en un rango de fechas
        return self.avl_tree.max_in_range(fecha1, fecha2)

    def min_temp_rango(self, fecha1, fecha2): # Devuelve la temperatura mínima en un rango de fechas
        return self.avl_tree.min_in_range(fecha1, fecha2)

    def temp_extremos_rango(self, fecha1, fecha2): # Devuelve las temperaturas mínima y máxima en un rango de fechas
        return self.avl_tree.extreme_in_range(fecha1, fecha2)

    def borrar_temperatura(self, fecha): # Borra la temperatura para una fecha dada
        if self.avl_tree.delete(fecha):
            self.sample_count -= 1

    def devolver_temperaturas(self, fecha1, fecha2): # Devuelve todas las temperaturas en un rango de fechas
        return self.avl_tree.get_records_in_range(fecha1, fecha2)

    def cantidad_muestras(self): # Devuelve la cantidad total de muestras almacenadas
        return self.sample_count

    def cargar_muestras_desde_archivo(self, filepath): # Carga muestras de un archivo y las guarda en el árbol
        with open(filepath, 'r') as file: 
            for line in file:
                fecha, temperatura = line.strip().split(';')
                self.guardar_temperatura(float(temperatura), fecha)
