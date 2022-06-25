class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print(self, prefix): 
        print(prefix + '(X): ' + str(self.x))
        print(prefix + '(Y): ' + str(self.y))


class Rectangle:
    def __init__(self, origin, width, height):
        self.origin = origin
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def print(self):
        top_right = self.origin.x + self.width
        bottom_left = self.origin.y + self.height
        self.origin.print()
        print('End Point X-Axis (Top Right): ' + str(top_right))
        print('End Point Y-Axis (Bottom Left): ' + str(bottom_left))


def build_rectangle():
    rectangle_point = Point(50, 100)
    rectangle = Rectangle(rectangle_point, 90, 10)

    return rectangle


rectangle = build_rectangle()

print(rectangle.calculate_area())
rectangle.print()