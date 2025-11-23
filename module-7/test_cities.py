# Tanner Elston, 11/19/25, Assignment Test Cases 7.2

import unittest
from city_functions import city_country

# Make assert methods available
class CityTestCase(unittest.TestCase):

# Utilize assert equal method, i.e. (a == b)
    def test_city_country(self):
        formatted = city_country('santiago', 'chile')
        self.assertEqual(formatted, 'Santiago, Chile')

if __name__ == "__main__":
    unittest.main()
