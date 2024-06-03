import unittest 

from calculadoraMatias import sumar
from calculadoraMatias import restar
from calculadoraMatias import multiplicar
from calculadoraMatias import dividir

class TestSumar(unittest.TestCase):
    def test_sumar_positivos(self):
        self.assertEqual(sumar(2,3), 5)

    def test_sumar_negativos(self):
        self.assertEqual(sumar(-2,-3), -5)

    def test_sumar_mixto(self):
        self.assertEqual(sumar(-2, 3), 1)

    def test_sumar_flotantes(self):
        self.assertAlmostEqual(sumar(1.3,0.6), 1.9)

    def test_sumar_numeros_grandes(self):
        self.assertEqual(sumar(2000000, 3000000), 5000000)

    def test_sumar_cero(self):
        self.assertEqual(sumar(0, 0), 0)

class TestRestar(unittest.TestCase):
    def test_restar_positivos(self):
        self.assertEqual(restar(4,3), 1)
    
    def test_restar_negativos(self):
        self.assertEqual(restar(-4, -3), -1)
    
    def test_restar_mixto(self):
        self.assertEqual(restar(-2, 3), -5)

    def test_restar_flotantes(self):
        self.assertEqual(restar(1.5, 0.7), 0.8)

    def test_restar_numeros_grandes(self):
        self.assertEqual(restar(3000000, 2000000), 1000000)

    def test_restar_cero(self):
        self.assertEqual(restar(0, 0), 0)

class TestMultiplicar(unittest.TestCase):
    def test_multiplicar_positivos(self):
        self.assertEqual(multiplicar(5, 5), 25)

    def test_multiplicar_negativos(self):
        self.assertEqual(multiplicar(-5, -5), 25)

    def test_multiplicar_negativo(self):
        self.assertEqual(multiplicar(-2,3), -6)

    def test_multiplicar_numeros_grandes(self):
        self.assertAlmostEqual(multiplicar(3000000, 4000000), 1.2e+13)
    
    def test_multiplicar_flotantes(self):
        self.assertAlmostEqual(multiplicar(1.5, 3.2), 4.8)

    def test_multiplicar_cero(self):
        self.assertEqual(multiplicar(0, 5), 0)
        self.assertEqual(multiplicar(5, 0), 0)

class TestDividir(unittest.TestCase):
    def test_dividir_positivos(self):
        self.assertEqual(dividir(6,2), 3)

    def test_dividir_negativos(self):
        self.assertEqual(dividir(-6, -2), 3)

    def test_dividir_negativo(self):
        self.assertEqual(dividir(-6, 2), -3)
    
    def test_dividir_flotantes(self):
        self.assertAlmostEqual(dividir(1.5, 0.5), 3.0)

    def test_dividir_numeros_grandes(self):
        self.assertAlmostEqual(dividir(5000000, 2), 2500000)

    def test_dividir_por_cero(self):
        with self.assertRaises(ZeroDivisionError):
            dividir(4, 0)
    
    def test_dividir_al_cero(self):
        self.assertEqual(dividir(0, 4), 0)

if __name__ == "__main__":
    unittest.main()