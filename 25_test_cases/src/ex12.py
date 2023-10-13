"""
Execise 12
"""


def get_smallest(num_list):
    """
    Get the smallest number from a list of numbers.

    Args:
        num_list (list): A list of numbers.

    Returns:
        int or None: The smallest number from the list. If the list is empty, returns None.
    """
    len_list = num_list.__len__()

    if  len_list == 0 :
        return None
    else :
        num_list.sort()
        return num_list[0]