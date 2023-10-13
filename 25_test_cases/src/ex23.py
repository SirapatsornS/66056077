"""
Exercise 23 : 99 Bottles of Beer on the Wall
"""


def bottles_of_beer(bottle):
    """
    Calculate the number of bottles of beer on the wall.
    And print out like this :

    99 bottles of beer on the wall,
    99 bottles of beer.
    Take one down, pass it around,
    98 bottles of beer on the wall.
    ...
    1 bottle of beer on the wall,
    1 bottle of beer.
    Take one down, pass it around,
    No more bottles of beer on the wall!

    Returns:
        str: The repeated lyrics of bottles of beer on the wall.
    """
    # FIX : complete this
    strout = ''
    if bottle != 1:
        strout += str(bottle) + ' bottles of beer on the wall,\n'
        strout += str(bottle) + ' bottles of beer.\n'
        strout += 'Take one down, pass it around,\n'
        if (bottle - 1) == 1:
            strout += '1 bottle of beer on the wall.\n'
        else:
            strout += str(bottle - 1) + ' bottles of beer on the wall.\n'
    else:
        strout += '1 bottle of beer on the wall,\n'
        strout += '1 bottle of beer.\n'
        strout += 'Take one down, pass it around,\n'
        strout += 'No more bottles of beer on the wall!\n'
    return strout
def loop_bottles_of_bears(bottle):
    while bottle > 0:
        print(bottles_of_beer(bottle))
        bottle -= 1


if __name__ == '__main__':
    loop_bottles_of_bears(5)
