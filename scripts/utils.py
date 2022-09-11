import scipy.stats


def cohen_d(x, y):
    """Returns the Cohen's d estimator of the effect size.

    See https://en.wikipedia.org/wiki/Effect_size#Cohen's_d for the
    actual formula implemented in this funciton.

    Args:
        x: An array-like containing samples drawn from the first
            population.
        y: An array-like containing samples drawn from the second
            population.

    Returns:
        The value of the Cohen's d estimator computed for the given
        parameters.
    """

    n_x = len(x)
    n_y = len(y)
    degrees_of_freedom = n_x + n_y - 2
    pooled_std = (((n_x - 1) * x.std(ddof=1) ** 2
        + (n_y - 1) * y.std(ddof=1) ** 2) / degrees_of_freedom) ** 0.5
    return (x.mean() - y.mean()) / pooled_std


def mean_test(x, mu):
    """ Perform the mean test:
        - Is the mean of the input (x) greater or equal to the
            expected mean (mu)?
        - Is it statistically significant?

    See https://www.w3schools.com/statistics/statistics_hypothesis_testing_mean.php
    for more details, including the actual formula implemented in this
    funciton.

    Args:
        x: An array-like containing samples drawn from a randomly
            selected population.

    Returns:
        A tuple of the form (statistic, p_value) where statistic is
        proportional to the difference between the input (x) mean and
        the expected mean (mu) and p_value is the level of significance.
    """

    n_x = len(x)
    statistic = (x.mean() - mu) * (n_x ** 0.5) / x.std(ddof=1)
    p_value =  1 - scipy.stats.t.cdf(statistic, n_x - 1)
    return statistic, p_value
