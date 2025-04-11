import unittest

from _testcapi import frozenset_new

from suma import Suma


class TestSuma(unittest.TestCase):
    def test_suma_dosNumeros_retornaSuma(self):
        # Arrange
        operando1 = 10
        operando2 = 15

        resultadoEsperado = 25

        objSuma = Suma(operando1, operando2)

        # Act
        resultadoActual = objSuma.calcularSuma()

        # Assert
        self.assertEqual(resultadoEsperado, resultadoActual, "fallo la suma")

def test_suma_operadorNoNumerico_lanzaException(self):
    objSuma=Suma(3,"a")
    with self.assertRaises(ValueError):
        objSuma.calcularSuma()


if __name__ == '__main__':
    unittest.main()
