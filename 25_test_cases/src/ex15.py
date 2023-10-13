"""
Exercise 15
"""


def median(num_list):
    """
    Calculate the median of a list of numbers.

    Parameters:
        num_list (list): A list of numbers.

    Returns:
        [int, None]: The median value of the list, or None if the list is empty.
    """
    num_list.sort()
    cal_len = num_list.__len__()
    index_median = cal_len//2

    if cal_len == 0:
        return None
    elif cal_len % 2 == 0 :
        cal_median = (num_list[index_median] + num_list[index_median-1])/2
        return cal_median
    else :
        cal_median = num_list[index_median]
        return cal_median
