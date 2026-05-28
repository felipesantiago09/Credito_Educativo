import unittest
from src.model.logica_Credito import (
    calcular_cuota,
    calcular_total_abonos,
    calcular_total_intereses,
    ErrorValorCompra,
    ErrorPlazo,
    ErrorDatos,
    ErrorUsura,
)

class CreditCardTest(unittest.TestCase):

    def test_normal_1(self):
        compra = 20000000
        interes = 1.2 / 100
        plazo = 60
        cuota = 469_523
        total_abonos = 28_171_374
        total_interes = 8_171_374
        self.assertAlmostEqual(cuota, calcular_cuota(compra, interes, plazo), 0)
        self.assertAlmostEqual(total_abonos, calcular_total_abonos(compra, interes, plazo), 0)
        self.assertAlmostEqual(total_interes, calcular_total_intereses(compra, interes, plazo), 0)

    def test_normal_2(self):
        compra = 35000000
        interes = 1.5 / 100
        plazo = 72
        cuota = 798273
        total_abonos = 57_475_634
        total_interes = 22_475_634
        self.assertAlmostEqual(cuota, calcular_cuota(compra, interes, plazo), 0)
        self.assertAlmostEqual(total_abonos, calcular_total_abonos(compra, interes, plazo), 0)
        self.assertAlmostEqual(total_interes, calcular_total_intereses(compra, interes, plazo), 0)

    def test_normal_3(self):
        compra = 15_000_000
        interes = 1.0 / 100
        plazo = 48
        cuota = 395_008
        total_abonos = 18_960_362
        total_interes = 3_960_362
        self.assertAlmostEqual(cuota, calcular_cuota(compra, interes, plazo), 0)
        self.assertAlmostEqual(total_abonos, calcular_total_abonos(compra, interes, plazo), 0)
        self.assertAlmostEqual(total_interes, calcular_total_intereses(compra, interes, plazo), 0)

    def test_caso_extraordinario_1(self):
        compra = 25_000_000
        interes = 0.9 / 100
        plazo = 96
        cuota_esperada = 390_019
        total_abonos = 37_441_815
        total_intereses = 12_441_815
        self.assertAlmostEqual(cuota_esperada, calcular_cuota(compra, interes, plazo), 0)
        self.assertAlmostEqual(total_abonos, calcular_total_abonos(compra, interes, plazo), 0)
        self.assertAlmostEqual(total_intereses, calcular_total_intereses(compra, interes, plazo), 0)

    def test_caso_extraordinario_2(self):
        compra = 18_000_000
        interes = 0.8 / 100
        plazo = 60
        cuota_esperada = 378_914
        total_abonos = 22_734_825
        total_intereses = 4_734_825
        self.assertAlmostEqual(cuota_esperada, calcular_cuota(compra, interes, plazo), 0)
        self.assertAlmostEqual(total_abonos, calcular_total_abonos(compra, interes, plazo), 0)
        self.assertAlmostEqual(total_intereses, calcular_total_intereses(compra, interes, plazo), 0)

    def test_caso_extraordinario_3(self):
        compra = 22_000_000
        interes = 1.3 / 100
        plazo = 36
        cuota_esperada = 769_117
        total_abonos = 27_688_218
        total_intereses = 5_688_218
        self.assertAlmostEqual(cuota_esperada, calcular_cuota(compra, interes, plazo), 0)
        self.assertAlmostEqual(total_abonos, calcular_total_abonos(compra, interes, plazo), 0)
        self.assertAlmostEqual(total_intereses, calcular_total_intereses(compra, interes, plazo), 0)

    def test_compra_cero(self):
        with self.assertRaises(ErrorValorCompra):
            calcular_cuota(-10_000_000, 2.4 / 100, 60)

    def test_plazo_mayor(self):
        with self.assertRaises(ErrorPlazo):
            calcular_cuota(80000, 2.4 / 100, 200)

    def test_plazo_invalido(self):
        with self.assertRaises(ErrorPlazo):
            calcular_cuota(50000, 12.4 / 100, -12)

    def test_datos_incompletos(self):
        with self.assertRaises(ErrorDatos):
            calcular_cuota(None, None, None)

if _name_ == '_main_':
    unittest.main()