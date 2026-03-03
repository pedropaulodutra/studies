def fahrenheit_to_celsius(fahrenheit_degree) -> str:
    """
    doctest:
    >>> fahrenheit_to_celsius(32)
    '0°C'
    """
    try:
        fahrenheit = int(fahrenheit_degree)
        celsius = int(5 * ((fahrenheit - 32) / 9))
        return f'{celsius}°C'
    except ValueError:
        raise ValueError('You must enter a number to convert.')
    
def celsius_to_fahrenheit(celsius_degree) -> str:
    """
    doctest:
    >>> celsius_to_fahrenheit(0)
    '32°F'
    """
    try:
        celsius = int(celsius_degree)
        fahrenheit = int(celsius * (9 / 5) + 32)
        return f'{fahrenheit}°F'
    except ValueError:
        raise ValueError('You must enter a number to convert.')

def main():
    choice = input('Choose "F" to convert °F to °C or "C" to convert °C to °F: ')
    temperature = input('Enter the temperature: ')
    match choice:
        case 'F':            
            celsius = fahrenheit_to_celsius(temperature)
            print(celsius)
        case 'C':
            fahrenheit = celsius_to_fahrenheit(temperature)
            print(fahrenheit)
        
if __name__ == '__main__':
    main()