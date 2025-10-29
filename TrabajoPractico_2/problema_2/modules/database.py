from avl_tree import AVLTree
class Temperaturas_DB:
    def __init__(self):
        self.avl_tree = AVLTree()
        self.sample_count = 0

    def guardar_temperatura(self, temperatura, fecha):
        self.avl_tree.insert(fecha, temperatura)
        self.sample_count += 1

    def devolver_temperatura(self, fecha):
        return self.avl_tree.search(fecha)

    def max_temp_rango(self, fecha1, fecha2):
        return self.avl_tree.max_in_range(fecha1, fecha2)

    def min_temp_rango(self, fecha1, fecha2):
        return self.avl_tree.min_in_range(fecha1, fecha2)

    def temp_extremos_rango(self, fecha1, fecha2):
        return self.avl_tree.extreme_in_range(fecha1, fecha2)

    def borrar_temperatura(self, fecha):
        if self.avl_tree.delete(fecha):
            self.sample_count -= 1

    def devolver_temperaturas(self, fecha1, fecha2):
        return self.avl_tree.get_records_in_range(fecha1, fecha2)

    def cantidad_muestras(self):
        return self.sample_count

    def cargar_muestras_desde_archivo(self, filepath):
        with open(filepath, 'r') as file:
            for line in file:
                fecha, temperatura = line.strip().split(';')
                self.guardar_temperatura(float(temperatura), fecha)
