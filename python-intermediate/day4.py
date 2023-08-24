class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y

    def __str__(self) -> str:
        return f"{self.x}, {self.y}"

    pass


point1 = Point(1, 2)
point2 = Point(1, 2)
print(point1)
print(point1 == point2)
