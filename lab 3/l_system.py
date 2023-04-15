import turtle


def apply(c):
    if c == "X":
        return "F+[[X]-X]-F[-FX]+X"
    elif c == "F":
        return "FF"
    else:
        return c


def transform(original):
    result = ""
    for c in original:
        result += apply(c)
    return result


def create_l_system(n, start):
    original = start
    for _ in range(n):
        result = transform(original)
        original = result
    return original


def draw_l_system(t, instructions, angle, length):
    stack = []
    for c in instructions:
        if c in ["F"]:
            t.forward(length)
        elif c == "-":
            t.right(angle)
        elif c == "+":
            t.left(angle)
        elif c == "[":
            stack.append((t.position(), t.heading()))
        elif c == "]":
            position, heading = stack.pop()
            t.pu()
            t.goto(position)
            t.setheading(heading)
            t.pd()

def draw():
    screen = turtle.Screen()
    t = turtle.Turtle()
    t.left(90)
    t.pu()
    t.back(200)
    t.pd()
    t.speed(5)
    instructions = create_l_system(5, "X")
    draw_l_system(t,instructions,25,5)
    screen.exitonclick()