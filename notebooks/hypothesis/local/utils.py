import numpy as np

def cohen_d(x, y):
    """Returns the Cohen's d estimator of the effect size.

    See https://en.wikipedia.org/wiki/Effect_size#Cohen's_d for the actual formula implemented in
    this funciton.

    Args:
        x: An array-like containing samples drawn from the first population.
        y: An array-like containing samples drawn from the second population.

    Returns:
        The value of the Cohen's d estimator computed for the given parameters.
    """

    n_x = len(x)
    n_y = len(y)
    degrees_of_freedom = n_x + n_y - 2
    pooled_std = (((n_x - 1) * np.var(x, ddof=1) + (n_y - 1) * np.var(y, ddof=1)) / degrees_of_freedom) ** 0.5
    return (np.mean(x) - np.mean(y)) / pooled_std
