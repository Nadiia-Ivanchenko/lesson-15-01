class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        return self.get_square() == other.get_square()

    def __add__(self, other):
        new_width = self.width + other.width
        new_height = self.height + other.height
        return Rectangle(new_width, new_height)

    def __mul__(self, n):
        new_width = self.width * n
        new_height = self.height * n
        return Rectangle(new_width, new_height)

    def __str__(self):
        return f"Rectangle (Width: {self.width}, Height: {self.height})"

