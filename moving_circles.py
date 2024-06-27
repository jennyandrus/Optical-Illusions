import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def draw_moving_circles():
    # Parameters
    n_circles = 10
    circle_spacing = 1.5
    max_radius = 0.5
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.axis('off')

    # Generate grid of circles
    circles = []
    for i in range(n_circles):
        for j in range(n_circles):
            circle = plt.Circle((i * circle_spacing, j * circle_spacing), max_radius, color='black')
            ax.add_patch(circle)
            circles.append(circle)

    def update(frame):
        for circle in circles:
            radius = max_radius * (1 + 0.5 * np.sin(frame * 0.1 + circle.center[0] + circle.center[1]))
            circle.set_radius(radius)

    ani = FuncAnimation(fig, update, frames=np.arange(0, 100, 1), interval=50)
    plt.xlim(-1, n_circles * circle_spacing)
    plt.ylim(-1, n_circles * circle_spacing)
    plt.show()

draw_moving_circles()
