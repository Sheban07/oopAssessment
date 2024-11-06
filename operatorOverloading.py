class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

vector1 = Vector(2, 3)  # Vector with components (2, 3)
vector2 = Vector(4, 1)  # Vector with components (4, 1)

result = vector1 + vector2

print(f"Result of vector addition: {result}")