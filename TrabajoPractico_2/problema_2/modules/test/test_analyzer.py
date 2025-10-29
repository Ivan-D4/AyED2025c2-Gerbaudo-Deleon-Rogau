import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from analyzer import calcular_promedio_temperaturas, generar_reporte_temperaturas
from database import Temperaturas_DB

class TestAnalyzer(unittest.TestCase):

    def setUp(self):
        self.db = Temperaturas_DB()
        self.db.guardar_temperatura(20.5, "01/01/2025")
        self.db.guardar_temperatura(25.0, "02/01/2025")
        self.db.guardar_temperatura(15.0, "03/01/2025")
        self.db.guardar_temperatura(30.0, "04/01/2025")

    def test_calcular_promedio_temperaturas(self):
        promedio = calcular_promedio_temperaturas(self.db, "01/01/2025", "04/01/2025")
        self.assertAlmostEqual(promedio, 22.625, places=2)

    def test_generar_reporte_temperaturas(self):
        reporte = generar_reporte_temperaturas(self.db, "01/01/2025", "04/01/2025")
        self.assertIn("01/01/2025: 20.5 ºC", reporte)
        self.assertIn("02/01/2025: 25.0 ºC", reporte)
        self.assertIn("03/01/2025: 15.0 ºC", reporte)
        self.assertIn("04/01/2025: 30.0 ºC", reporte)

if __name__ == '__main__':
    unittest.main()