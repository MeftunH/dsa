# set circular algorithm

import numpy as np
import matplotlib.pyplot as plt
import math

def circular_algorithm(x, y, r, n):
    """
    x, y: center of the circle
    r: radius of the circle
    n: number of points
    """
    points = []
    for i in range(n):
        angle = 2 * math.pi * i / n
        points.append((x + r * math.cos(angle), y + r * math.sin(angle)))
    return points

def plot_circle(x, y, r, n):
    points = circular_algorithm(x, y, r, n)
    points.append(points[0])
    x, y = zip(*points)
    plt.plot(x, y)
    plt.show()

plot_circle(0, 0, 1, 100)
plot_circle(1, 1, 1, 100)
plot_circle(2, 2, 1, 100)
plot_circle(3, 3, 1, 100)
plot_circle(4, 4, 1, 100)