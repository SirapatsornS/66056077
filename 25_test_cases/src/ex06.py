"""
Execise 6
"""


def ordinal_suffix(number):
    """
    Return the ordinal suffix for a given number.

    Parameters:
        num (int): The number for which to find the ordinal suffix.

    Returns:
        str: The ordinal suffix corresponding to the given number.
    """
    # TODO : complete this
    last_num = int(str(number)[-1:])
    last_2num = int(str(number)[-2:])
    len_num = (len(str(number)))
    if last_num == 1 and last_2num != 11:
        return f'{number}st'
    elif last_num == 2 and last_2num != 12 :
        return f'{number}nd'
    elif last_num == 3 and last_2num != 13 :
        return f'{number}rd'
    else :
        return f'{number}th'

#%%
