"""
Execise 2
"""


def convert_to_fahrenheit(celsius=0):
    """
    Convert Celsius temperature to Fahrenheit.

    Args:
        celsius (float): The temperature in Celsius.

    Returns:
        float: The temperature in Fahrenheit.
    """
    # FIX : complete this
    fahrenheit = (9/5) * celsius + 32
    return round(fahrenheit)


def convert_to_celsius(fahrenheit= 0):
    """
    Convert a temperature from Fahrenheit to Celsius.

    Parameters:
    - fahrenheit (float): The temperature in Fahrenheit.

    Returns:
    - float: The temperature in Celsius.
    """
    # FIX : complete this
    celsius = (fahrenheit - 32) * (5/9)
    return round(celsius)
