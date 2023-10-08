"""
Execise 3
"""


def is_odd(num):
    """
    Check if a number is odd.

    Args:
        num (int): The number to be checked.

    Returns:
        bool: True if the number is odd, False otherwise.
    """
    # FIX : complete this
    number = num % 2
    return number == 1

def is_even(num):
    """
    Determines if a given number is even.

    Parameters:
        num (int): The number to be checked.

    Returns:
        bool: True if the number is even, False otherwise.
    """
    # FIX : complete this
    number = num % 2
    return number == 0
