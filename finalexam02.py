import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Point(x: {self.x}, y: {self.y})"


if __name__ == "__main__":
    p1 = Point(1, 1)
    p2 = Point(2, 2)
    print("distance:", p1.distance(p2))

    p3 = p1 + p2
    print("p1 + p2 =", p3)
