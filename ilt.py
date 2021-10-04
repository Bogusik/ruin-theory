from mpmath import *

# Decimal points precision.
mp.dps = 4


# Returns numeric inverse Laplace transform of the first model ruin probability function.
def get_ilt_first(u: float) -> float:
    def laplace_transform(p: float):
        return (1 - (1 * 2.25 / 4.5)) / (
                p * (1 - (1 / 4.5) *
                     (0.35 * exp(-4 * p) / (p ** 2) - 0.35 * exp(-2 * p) / (
                             p ** 2) + 0.3 * exp(-p) / (p ** 2) - 0.3 / (
                              p ** 2) + 1 / p)
                     ))

    return invertlaplace(laplace_transform, u, method='talbot')


# Returns numeric inverse Laplace transform of the second model ruin probability function.
def get_ilt_second(u: float) -> float:
    def laplace_transform(p: float):
        return (1 - (5 * 2.25 / 11.8125)) / (
                p * (1 - (5 / 11.8125) *
                     (0.35 * exp(-4 * p) / (p ** 2) - 0.35 * exp(-2 * p) / (
                             p ** 2) + 0.3 * exp(-p) / (p ** 2) - 0.3 / (
                              p ** 2) + 1 / p)
                     ))

    return invertlaplace(laplace_transform, u, method='talbot')
