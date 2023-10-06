from carea.shape import Shape
class Oval(Shape):

    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.oval_area = 0.0

    def __str__(self) -> str:
        return 'Oval Area radius ' + str(self.width) + ' & ' + str(self.height) + ' is ' + str(self.area())
    def area(self):
        self.oval_area = 3.14 * self.width * self.height
        return self.oval_area