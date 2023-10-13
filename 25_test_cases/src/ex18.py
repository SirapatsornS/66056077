"""
Exercise 18 : Buy 8 get 1 free
"""


def get_cost_of_coffee(amountcoff, price):
    freecoff = amountcoff // 9
    diffprice = amountcoff - freecoff
    return diffprice * price

def get_cost_of_coffee_2(numcoff, price):
    freecoff = numcoff // 9
    diffprice = numcoff - freecoff
    return diffprice * price

