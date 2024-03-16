import turtle

def draw_spiral(t, line_len):
    if line_len > 0:
        t.forward(line_len)
        t.right(90)
        draw_spiral(t, line_len - 5)

def main():
    t = turtle.Turtle()
    my_win = turtle.Screen()
    t.speed(0)
    draw_spiral(t, 100)
    my_win.exitonclick()
