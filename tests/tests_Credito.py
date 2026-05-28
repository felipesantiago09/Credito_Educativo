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

    # Cada prueba unitaria es un metodo la clase
    def test_normal_1(self):
        # ENTRADAS
        compra = 20000000
        interes = 1.2 / 100
        plazo = 60
        cuota = 469_523
        #SALIDAS ESPERADAS
        total_abonos = 28_171_374
        total_interes = 8_171_374

        cuota_calculada = logica_Credito.calcular_cuota( compra, interes, plazo )
        total_abonos_calculado = logica_Credito.calcular_total_abonos( compra, interes, plazo )
        total_intereses_calculado = logica_Credito.calcular_total_intereses( compra, interes, plazo)

        # Prueba que dos variables sean iguales
        self.assertAlmostEqual( cuota, cuota_calculada, 0 )
        self.assertAlmostEqual( total_abonos, total_abonos_calculado, 0 )
        self.assertAlmostEqual( total_interes, total_intereses_calculado, 0 )

    def test_normal_2(self):
        compra = 35000000 
        interes = 1.5 / 100
        plazo = 72
        cuota = 798273

        total_abonos = 57_475_634
        total_interes = 22_475_634

        
        cuota_calculada = logica_Credito.calcular_cuota( compra, interes, plazo )
        total_abonos_calculado = logica_Credito.calcular_total_abonos( compra, interes, plazo )
        total_intereses_calculado = logica_Credito.calcular_total_intereses( compra, interes, plazo)

        # Prueba que dos variables sean iguales
        self.assertAlmostEqual( cuota, cuota_calculada, 0 )
        self.assertAlmostEqual( total_abonos, total_abonos_calculado, 0  )
        self.assertAlmostEqual( total_interes, total_intereses_calculado, 0 )

    def test_normal_3(self):
        compra = 15_000_000
        interes = 1.0 / 100
        plazo = 48
        cuota = 395_008

        total_abonos = 18_960_362
        total_interes = 3_960_362

        cuota_calculada = logica_Credito.calcular_cuota( compra, interes, plazo )
        total_abonos_calculado = logica_Credito.calcular_total_abonos( compra, interes, plazo )
        total_intereses_calculado = logica_Credito.calcular_total_intereses( compra, interes, plazo)

        self.assertAlmostEqual( cuota, cuota_calculada, 0)
        self.assertAlmostEqual( total_abonos, total_abonos_calculado, 0 )
        self.assertAlmostEqual( total_interes, total_intereses_calculado, 0 )

    def test_caso_extraordinario_1(self):
        # ENTRADAS
        compra = 25_000_000
        interes = 0.9 / 100
        plazo = 96
        #SALIDAS ESPERADAS
        cuota_esperada = 390_019
        total_abonos = 37_441_815
        total_intereses = 12_441_815

        cuota_calculada = logica_Credito.calcular_cuota( compra, interes, plazo )
        total_abonos_calculado = logica_Credito.calcular_total_abonos( compra, interes, plazo )
        total_intereses_calculado = logica_Credito.calcular_total_intereses( compra, interes, plazo)

        # Prueba que dos variables sean iguales
        self.assertAlmostEqual( cuota_esperada, cuota_calculada, 0 )
        self.assertAlmostEqual( total_abonos, total_abonos_calculado, 0  )
        self.assertAlmostEqual( total_intereses, total_intereses_calculado, 0 )
    
    def test_caso_extraordinario_2(self):
        compra = 18_000_000
        interes = 0.8 / 100
        plazo = 60 

        cuota_esperada = 378_914
        total_abonos = 22_734_825
        total_intereses = 4_734_825

        cuota_calculada = logica_Credito.calcular_cuota( compra, interes, plazo )
        total_abonos_calculado = logica_Credito.calcular_total_abonos( compra, interes, plazo )
        total_intereses_calculado = logica_Credito.calcular_total_intereses( compra, interes, plazo)

        self.assertAlmostEqual( cuota_esperada, cuota_calculada, 0 )
        self.assertAlmostEqual( total_abonos, total_abonos_calculado, 0  )
        self.assertAlmostEqual( total_intereses, total_intereses_calculado, 0 )

    def test_caso_extraordinario_3(self):
        compra = 22_000_000
        interes = 1.3 / 100
        plazo = 36

        cuota_esperada = 769_117
        total_abonos = 27_688_218
        total_intereses = 5_688_218

        cuota_calculada = logica_Credito.calcular_cuota( compra, interes, plazo )
        total_abonos_calculado = logica_Credito.calcular_total_abonos( compra, interes, plazo )
        total_intereses_calculado = logica_Credito.calcular_total_intereses( compra, interes, plazo)

        self.assertAlmostEqual( cuota_esperada, cuota_calculada, 0 )
        self.assertAlmostEqual( total_abonos, total_abonos_calculado, 0 )
        self.assertAlmostEqual( total_intereses, total_intereses_calculado, 0 )

    def test_compra_cero(self):
        # ENTRADAS
        compra = -10_000_000
        interes = 2.4 / 100
        plazo = 60
        #SALIDAS ESPERADAS

        # Verifica que si se genere una excepcion adentro del bloque with
        with self.assertRaises( logica_Credito.ErrorValorCompra ) :
            cuota_calculada = logica_Credito.calcular_cuota( compra, interes, plazo )

    def test_plazo_mayor( self ):
        # ENTRADAS
        compra = 80000
        interes = 2.4 / 100
        plazo = 200
        #SALIDAS ESPERADAS

        # Verifica que si se genere una excepcion adentro del bloque with
        with self.assertRaises( logica_Credito.ErrorPlazo ) :
            cuota_calculada = logica_Credito.calcular_cuota( compra, interes, plazo )

    def test_plazo_invalido( self ):
        compra = 50000
        tasa = 12.4 / 100
        plazo = -12 
        with self.assertRaises( logica_Credito.ErrorPlazo) :
            cuota_calculada = logica_Credito.calcular_cuota( compra, tasa, plazo )
    
    def test_datos_incompletos( self ):
        compra = None 
        tasa = None 
        plazo = None 

        with self.assertRaises( logica_Credito.ErrorDatos ) : 
            cuota_calculada = logica_Credito.calcular_cuota( compra, tasa, plazo )

# Este fragmento de codigo permite ejecutar la prueb individualmente
# Va fijo en todas las pruebas
if __name__ == '__main__':
    # print( Payment.calcularCuota.__doc__)
    unittest.main()