import random

def approximate_pi(num_points):
    points_inside_circle = 0
    points_total = num_points

    for _ in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x ** 2 + y ** 2 < 1:
            points_inside_circle += 1

    pi_approximation = 4 * points_inside_circle / points_total
    return pi_approximation

# Main program
num_points = int(input("Enter the number of random points to generate: "))
approximation = approximate_pi(num_points)
print("Approximation of pi:", approximation)