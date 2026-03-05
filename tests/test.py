from pytest import mark, raises

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


@mark.f2c
def test_f2c_should_retun_valueerror_when_receiving_string():
    with raises(ValueError):
        fahrenheit_to_celsius('a')

@mark.c2f
def test_c2f_should_return_valueerror_when_receiving_string():
    with raises(ValueError):
        celsius_to_fahrenheit('a')
