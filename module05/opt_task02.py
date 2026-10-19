import numpy as np
import matplotlib.pyplot as plt


def estimate_PI(num_points, seed=None):
    """Estimate PI using Monte Carlo simulation."""

    # Create random number generator
    rng = np.random.default_rng(seed)

    # Generate random coordinates
    x = rng.random(num_points)
    y = rng.random(num_points)

    # Identify points inside the quadrant
    mask_circle = (x**2 + y**2 < 1)

    # Count points inside the circle
    inside_circle_count = np.sum(mask_circle)

    # Estimate PI
    pi_estimate = 4 * inside_circle_count / num_points

    return pi_estimate


if __name__ == '__main__':

    num_points_values = np.logspace(1, 6, 100, dtype=int)

    pi_estimates = []

    for n in num_points_values:
        pi_estimates.append(estimate_PI(n))

    pi_estimates = np.array(pi_estimates)

    percentage_deviation = (pi_estimates - np.pi) / np.pi * 100

    plt.semilogx(num_points_values, pi_estimates)
    plt.axhline(np.pi, color='red', linestyle='--', label='π')
    plt.xlabel('Number of points')
    plt.ylabel('Estimated π')
    plt.legend()
    plt.show()

    plt.semilogx(num_points_values, percentage_deviation)
    plt.axhline(0, color='red', linestyle='--')
    plt.xlabel('Number of points')
    plt.ylabel('Deviation from π [%]')
    plt.show()
