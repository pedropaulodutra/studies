from pytest import mark

from main import fahrenheit_to_celsius, celsius_to_fahrenheit


@mark.f2c
@mark.parametrize(
    'fahrenheit, celsius',
    [(32, '0°C'), (-40, '-40°C')]
)
def test_fahrenheit_to_celsius(fahrenheit, celsius):
    assert fahrenheit_to_celsius(fahrenheit) == celsius

@mark.c2f
@mark.parametrize(
    'celsius, fahrenheit',
    [(0, '32°F'), (-40, '-40°F')]
)
def test_celsius_to_fahrenheit(celsius, fahrenheit):
    assert celsius_to_fahrenheit(celsius) == fahrenheit

@mark.xfail
@mark.parametrize(
    'fahrenheit, celsius',
    [('a', '28°C'), ('81°F', 'b')]
)
def test_should_return_valueerror_when_receiving_a_string(fahrenheit, celsius):
    assert fahrenheit_to_celsius(fahrenheit) == celsius
    assert celsius_to_fahrenheit(celsius) == fahrenheit