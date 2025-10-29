import unittest
from src.database import Temperaturas_DB

class TestTemperaturasDB(unittest.TestCase):

    def setUp(self):
        self.db = Temperaturas_DB()
        self.db.guardar_temperatura(13.2, "01/01/2025")
        self.db.guardar_temperatura(38.6, "02/01/2025")
        self.db.guardar_temperatura(25.8, "03/01/2025")

    def test_guardar_temperatura(self):
        self.db.guardar_temperatura(21.1, "10/01/2025")
        self.assertEqual(self.db.devolver_temperatura("10/01/2025"), 21.1)

    def test_devolver_temperatura(self):
        self.assertEqual(self.db.devolver_temperatura("01/01/2025"), 13.2)
        self.assertIsNone(self.db.devolver_temperatura("nonexistent_date"))

    def test_max_temp_rango(self):
        self.assertEqual(self.db.max_temp_rango("01/01/2025", "03/01/2025"), 38.6)

    def test_min_temp_rango(self):
        self.assertEqual(self.db.min_temp_rango("01/01/2025", "03/01/2025"), 13.2)

    def test_temp_extremos_rango(self):
        min_temp, max_temp = self.db.temp_extremos_rango("01/01/2025", "03/01/2025")
        self.assertEqual(min_temp, 13.2)
        self.assertEqual(max_temp, 38.6)

    def test_borrar_temperatura(self):
        self.db.borrar_temperatura("01/01/2025")
        self.assertIsNone(self.db.devolver_temperatura("01/01/2025"))

    def test_devolver_temperaturas(self):
        temperaturas = self.db.devolver_temperaturas("01/01/2025", "03/01/2025")
        expected = [
            "01/01/2025: 13.2 ºC",
            "02/01/2025: 38.6 ºC",
            "03/01/2025: 25.8 ºC"
        ]
        self.assertEqual(temperaturas, expected)

    def test_cantidad_muestras(self):
        self.assertEqual(self.db.cantidad_muestras(), 3)

    def test_cargar_muestras_desde_archivo(self):
        self.db.cargar_muestras_desde_archivo("path/to/muestras.txt")
        self.assertGreater(self.db.cantidad_muestras(), 3)

if __name__ == '__main__':
    unittest.main()
    #no tengo ni idea por que no me deja subirlo
    