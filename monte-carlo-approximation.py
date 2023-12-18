import numpy as np
import math

def is_point_outside_circle(x, y, h, k, r):
    distance = math.sqrt((x - h)**2 + (y - k)**2)
    return distance > r

def monte_carlo_approximation(nr_iterations=100000):
    """
    Approximates the value of pi using the Monte Carlo method.
    """
    max_square_size = 1
    circle_radius = 1
    inside_circle = 0
    outside_circle = 0
    for _ in range(nr_iterations):
        random_point = np.random.uniform(-max_square_size, max_square_size, 2)
        if is_point_outside_circle(random_point[0], random_point[1], 0, 0, circle_radius):
            outside_circle += 1
        else:
            inside_circle += 1
        
        print(f"Random point: {random_point}")
        print(f" inside_circle: {inside_circle}, outside_circle: {outside_circle}, total {inside_circle + outside_circle}")
        print(f" Approximated π: {4 * inside_circle / (inside_circle + outside_circle)}")





if __name__ == "__main__":
    monte_carlo_approximation()