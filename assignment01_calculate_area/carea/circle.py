from carea.shape import Shape
class Circle(Shape):
    def __init__(self, radius):
        self.cc_area = 0.0
        self.radius = radius

    def area(self):
        self.cc_area = 3.14*self.radius * self.radius
        return self.cc_area

    def __str__(self) -> str:
        return 'Circle Area radius ' + str(self.radius) + ' is ' + str(self.area())