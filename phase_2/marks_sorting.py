class Marks:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value < other.value


marks = [
    Marks(85),
    Marks(60),
    Marks(95),
    Marks(75)
]

sorted_marks = sorted(marks)

for mark in sorted_marks:
    print(mark.value)