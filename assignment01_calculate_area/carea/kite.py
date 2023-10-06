from carea.shape import Shape
class Kite(Shape):
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.kite_area = 0.0

    def __str__(self) -> str:
        return 'Kite Area width ' + str(self.width) + ' height ' + str(self.height) + ' is ' + str(self.area())
    def area(self):
        self.kite_area = 0.5 * self.width * self.height
        return self.kite_area