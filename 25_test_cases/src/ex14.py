"""
Exercise 14
"""


def average(num_list: list) -> float:
    """
    Calculate the average of a list of numbers.

    Parameters:
    - num_list (list): A list of numbers.

    Returns:
    - float: The average of the numbers in the list.
      If the list is empty, returns 0.
    """
    len_list = num_list.__len__()
    sumnum = 0
    for i in num_list :
        sumnum = sumnum + i
    average = sumnum/len_list
    return average
