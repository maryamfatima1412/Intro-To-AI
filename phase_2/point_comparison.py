class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


p1 = Point(2, 3)
p2 = Point(2, 3)
p3 = Point(5, 6)

print(p1 == p2)
print(p1 == p3)