"""Module for drawing a Koch snowflake using the turtle graphics library."""

import turtle

def koch_curve(t, order, size):
    """
    Draws a Koch curve using turtle graphics.
    """
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def draw_koch_snowflake(order, size=400):
    """
    Draws a Koch snowflake of a given order and size.
    """
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)  # Максимальна швидкість малювання
    t.penup()
    t.goto(-size / 2, size / 3)
    t.pendown()

    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    window.mainloop()
    t.hideturtle()

def main():
    """Main function."""
    order = int(input("Вкажіть рівень рекурсії: "))
    draw_koch_snowflake(order)

if __name__ == "__main__":
    main()
