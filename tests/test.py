from unittest import TestCase

from main import fahrenheit_to_celsius, celsius_to_fahrenheit

class TestFahrenheitToCelsius(TestCase):
    def test_should_return_0_when_receiving_32(self):
        self.assertEqual(fahrenheit_to_celsius(32), '0°C')

    def test_should_not_return_1_when_receiving_0(self):
        self.assertNotEqual(fahrenheit_to_celsius(0), '1°C')

    def test_should_return_valueerror_when_receiving_strings(self):
        self.assertRaises(ValueError, fahrenheit_to_celsius, 'a')

class TestCelsiusToFahrenheit(TestCase):
    def test_should_return_32_when_receiving_0(self):
        self.assertEqual(celsius_to_fahrenheit(0), '32°F')

    def test_should_not_return_0_when_receiving_1(self):
        self.assertNotEqual(celsius_to_fahrenheit(1), '0°F')

    def test_should_return_valueerror_when_receiving_strings(self):
        self.assertRaises(ValueError, celsius_to_fahrenheit, 'a')