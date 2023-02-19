import math


class Point:
    def __init__(self, x = 0, y = 0):
        self.x = 0
        self.y = 0

    def __str__(self) -> str:
        return f"Point({self.x}, {self.y})"

class Segment:
   def __init__(self, p1, p2):
       self.p1 = p1
       self.p2 = p2
   def distance(self):
       return math.hypot(self.p1.x-self.p2.x, self.p1.y-self.p2.y)
def main():
    p = Point(3, 0)
    q = Point(0, 4)
    f = Segment(p, q)
    print(f.distance())


main()

