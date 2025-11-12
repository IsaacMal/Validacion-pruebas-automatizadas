import unittest
from src.procesador import Analizador
import os

class TestAnalizador(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Construir ruta absoluta al CSV, independientemente del directorio actual
        base_dir = os.path.dirname(os.path.dirname(__file__))  # sube a la raíz del proyecto
        ruta_csv = os.path.join(base_dir, "datos", "sri_ventas_2024.csv")
        cls.analizador = Analizador(ruta_csv)

    def test_ventas_totales_como_diccionario(self):
        resumen = self.analizador.ventas_totales_por_provincia()
        self.assertIsInstance(resumen, dict)

    def test_ventas_totales_todas_las_provincias(self):
        resumen = self.analizador.ventas_totales_por_provincia()
        total_provincias = len(resumen)
        # Siempre debe haber al menos 1 provincia
        self.assertGreaterEqual(total_provincias, 1)

    def test_ventas_totales_mayores_5k(self):
        resumen = self.analizador.ventas_totales_por_provincia()
        # Validar que al menos una provincia tenga ventas > 5000
        self.assertTrue(any(float(v) > 5000 for v in resumen.values()))

    def test_ventas_por_provincia_inexistente(self):
        # El método devuelve 0 si la provincia no existe
        resultado = self.analizador.ventas_por_provincia("Narnia")
        self.assertEqual(resultado, 0)

    def test_ventas_por_provincia_existente(self):
        resumen = self.analizador.ventas_totales_por_provincia()
        # Buscar automáticamente una provincia con ventas > 0
        provincia = next((p for p, v in resumen.items() if float(v) > 0), None)
        if provincia is None:
            self.skipTest("No hay provincias con ventas > 0 en el CSV")
        else:
            resultado = self.analizador.ventas_por_provincia(provincia)
            self.assertGreater(resultado, 0)


