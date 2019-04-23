import unittest
from hexa import hexa

class Test_decimal_hexadecimal(unittest.TestCase):

    def test_1_a_hexa(self):
        final = hexa(1)
        self.assertEqual(final, '1')
    
    def test_5_a_hexa(self):
        final = hexa(5)
        self.assertEqual(final, '5')

    def test_10_a_hexa(self):
        final = hexa(10)
        self.assertEqual(final, 'A')

    def test_15_a_hexa(self):
        final = hexa(15)
        self.assertEqual(final, 'F')

    def test_16_a_hexa(self):
        final = hexa(16)
        self.assertEqual(final, '10')

    def test_17_a_hexa(self):
        final = hexa(17)
        self.assertEqual(final, '11')

    def test_234_a_hexa(self):
        final = hexa(234)
        self.assertEqual(final, 'EA')

    def test_921_a_hexa(self):
        final = hexa(921)
        self.assertEqual(final, '399')
    
    def test_1234_a_hexa(self):
        final = hexa(1234)
        self.assertEqual(final, '4D2')
    
    def test_4095_a_hexa(self):
        final = hexa(4095)
        self.assertEqual(final, 'FFF')

    
    


if __name__ == "__main__":
    unittest.main()