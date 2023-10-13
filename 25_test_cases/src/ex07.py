"""
Execise 7
"""


def print_ASCII_table(fr,se):
    """
    Generate and print the ASCII table for a range of characters.

    Args:
        start_char (int): The ASCII value of the starting character.
        end_char (int): The ASCII value of the ending character.

    Returns:
        str: Returns nothing. The function simply prints the ASCII characters.

    """
    # FIX : complete this
    for i in range(fr,se+1):
        captured = chr(i)
        print(captured)
