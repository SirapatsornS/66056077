"""
Exercise 16
"""


def mode(num_list):
    """
    Calculate the mode of a list of numbers.

    Parameters:
    - num_list (list): A list of numbers.

    Returns:
    - int or None: The mode of the list, or None if the list is empty.
    """
    len_list = num_list.__len__()
    uniq_num = []
    mode_num = []

    if len_list > 0 :
        for i in num_list:
            if i not in uniq_num:
                uniq_num.append(i)
            else:
                mode_num.append(i)
        for n in mode_num :
            return n
    else :
        return None
