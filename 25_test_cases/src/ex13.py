"""
Exercise 13
"""


def calc_sum(num_list):
    """
    Calculate the sum of a list of numbers.

    Parameters:
    - num_list (list): A list of numbers.

    Returns:
    - int: The sum of all the numbers in the list.
    """
    return sum(num_list)


def calc_prod(num_list):
    """
    Calculates the product of all the numbers in the given list.

    Parameters:
        num_list (list): A list of numbers.

    Returns:
        int: The product of all the numbers in the list.
    """
    calc_prod = 1
    len_list = num_list.__len__()
    if  len_list == 0 :
        return calc_prod
    else :
        for i in num_list :
            calc_prod = calc_prod * i
        return calc_prod
