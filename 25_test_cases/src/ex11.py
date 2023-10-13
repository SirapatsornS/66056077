"""
Exercise 11
"""


def get_hr_min_sec(tsec=0):
    """
    Generates a string representation of the given number
    of seconds in the format "9h 9m 9s".

    Args:
        tsec (int): The number of seconds to convert to
        the "9h 9m 9s" format. Default is 0s.

    Returns:
        str: A string representation of the given
        number of seconds in the "9h 9m 9s" format.

    Example:
        >>> get_hr_min_sec(3665)
        '1h 1m 5s'
        >>> get_hr_min_sec(0)
        '0s'
    """

    if tsec == 0 :
        return f'{tsec}s'
    elif tsec > 0 :
        hour = tsec // 3600
        tsec %= 3600
        minutes = tsec // 60
        tsec %= 60

        if hour > 0 and minutes > 0 and tsec > 0 :
            return f'{hour}h {minutes}m {tsec}s'
        elif hour > 0 and minutes > 0 :
            return f'{hour}h {minutes}m'
        elif hour > 0 and tsec > 0 :
            return f'{hour}h {tsec}s'
        elif hour > 0 :
            return f'{hour}h'
        elif minutes > 0 and tsec > 0 :
            return f'{minutes}m {tsec}s'
        elif minutes > 0 :
            return f'{minutes}m'
        elif tsec > 0 :
            return f'{tsec}s'
        else :
            return ''