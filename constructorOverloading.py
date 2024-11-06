class Rectangle:
    def __init__(self, length, width=None):
        self.length = length
        self.width = width if width is not None else length

    def area(self):
        return self.length * self.width

square = Rectangle(5)
print(f"Square area: {square.area()}")

rectangle = Rectangle(4, 6)
print(f"Rectangle area: {rectangle.area()}")
