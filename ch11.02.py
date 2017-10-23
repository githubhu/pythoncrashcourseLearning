


def city_function(city, country):
    str=city + "," + country
    #print str
    return str

#city_function("hangzhou", "China")

import unittest

class CityTest(unittest.TestCase):
    def test_city_function(self):
        get_city_function=city_function("Hangzhou", "China")
        self.assertEqual(get_city_function, "Hangzhou,China")






