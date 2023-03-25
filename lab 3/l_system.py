import turtle


def apply(c):
    if c == "F":
        return "F+F-F-F+F"
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
    for c in instructions:
        if c == "F":
            t.forward(length)
        elif c == "-":
            t.right(angle)
        elif c == "+":
            t.left(angle)


def draw():
    screen = turtle.Screen()
    t = turtle.Turtle()

    t.speed(100)
    instructions = create_l_system(3, "F")
    draw_l_system(t,instructions,90,10)
    screen.exitonclick()