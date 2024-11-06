from abc import ABC, abstractmethod
import math

#abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# circle class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2

# square subclass
class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

circle = Circle(5)
square = Square(4)

print(f"Area of circle: {circle.area():.2f}")
print(f"Area of square: {square.area()}")
