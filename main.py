import math


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"Point({self.x}, {self.y})"


class Segment:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

        def __str__(self) -> str:
            return f"Segment({self.p1}, {self.p2})"

    def distance(self):
        return math.hypot(self.p1.x - self.p2.x, self.p1.y - self.p2.y)

    def svg(self):
        return f'<line x1="{self.p1.x}" y1="{self.p1.y}" x2="{self.p2.x}" y2"{self.p2.y}" style="stroke:black" />'

class Polygon:
    def __init__(self):
        self.vertices=[]

    def add(self,vertex):
        self.vertices.append(vertex)

    def __str__(self) -> str:
        vertices_str=""
        for vertex in self.vertices:
            vertices_str+=str(vertex) + ", "
        return f"Polygon({vertices_str[:-2]})"
    def svg(self):
        #<polygon points = "200, 10 250,190 160,210"/>
        vertices_str = ""
        for vertex in self.vertices:
            vertices_str += f'{vertex.x,},{vertex.y} '
        return f'<polygon points = "{vertices_str[:-1]}"/>'
def main():
    p = Point(300, 0)
    q = Point(0, 400)

    polygon=Polygon()
    polygon.add(p)
    polygon.add(q)
    polygon.add(Point(300,400))

    print(polygon.svg())



main()
