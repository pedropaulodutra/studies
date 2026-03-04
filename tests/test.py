from main import fahrenheit_to_celsius, celsius_to_fahrenheit


# Fahrenheit to Celsius
def test_should_return_0_when_receiving_32():
    assert fahrenheit_to_celsius(32) == '0°C'

def test_should_not_return_1_when_receiving_0():
    assert fahrenheit_to_celsius(0) != '1°C'


# Celsius to Fahrenheit
def test_should_return_32_when_receiving_0():
    assert celsius_to_fahrenheit(0) == '32°F'

def test_should_not_return_0_when_receiving_1():
    assert celsius_to_fahrenheit(1) != '0°F'
