import unittest
from interfaz_hexa import interfaz_hexa
from interfaz_hexa import Not_a_number_exception
from interfaz_hexa import Not_in_range_exception

class Test_decimal_hexadecimal(unittest.TestCase):

    def test_1_a_hexa(self):
        final = interfaz_hexa('1')
        self.assertEqual(final, '1')
    
    def test_5_a_hexa(self):
        final = interfaz_hexa('5')
        self.assertEqual(final, '5')

    def test_15_a_hexa(self):
        final = interfaz_hexa('15')
        self.assertEqual(final, 'F')

    def test_921_a_hexa(self):
        final = interfaz_hexa('921')
        self.assertEqual(final, '399')

    def test_4095_a_hexa(self):
        final = interfaz_hexa('4095')
        self.assertEqual(final, 'FFF')

    def test_hola_a_hexa(self):
        try:
            interfaz_hexa('hola')
            self.fail()
        except Not_a_number_exception:
            pass
    
    def test_negativo_a_hexa(self):
        try:
            interfaz_hexa('-2')
            self.fail()
        except Not_in_range_exception:
            pass
    
    def test_mas_4095_a_hexa(self):
        try:
            interfaz_hexa('5000')
            self.fail()
        except Not_in_range_exception:
            pass
            


if __name__ == "__main__":
    unittest.main()