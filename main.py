class Point:
    def __init__(self, x = 0, y = 0):
        self.x = 0
        self.y = 0

    def __str__(self) -> str:
        return f"Point({self.x}, {self.y})"


def main():
    p = Point()
    p.x = 100
    print(p.x, p.y)


main()

