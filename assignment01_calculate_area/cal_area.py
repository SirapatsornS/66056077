#cal_area
from carea.kite import Kite
from carea.circle import Circle
from carea.triangle import Triangle
from carea.oval import Oval

if __name__ == '__main__':
    cc1 = Circle(5)
    print(cc1)

    ov1 = Oval(5, 10)
    print(ov1)

    tria1 = Triangle(7, 10)
    print(tria1)

    kite1 = Kite(6, 12)
    print(kite1)