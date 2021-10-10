from mpmath import *

mp.dps = 4


def get_ilt_first(u: float) -> float:
    def laplace_transform(p: float):
        return 0.5 / (p - (1-0.5 * exp(-p) - 0.5 * exp(-10*p))/11)

    return invertlaplace(laplace_transform, u, method='talbot')


def get_ilt_second(u: float) -> float:
    def laplace_transform(p: float):
        return ((11/231) / (p - 40 * ((1-0.5 * exp(-p) - 0.5 * exp(-10*p))/231)))

    return invertlaplace(laplace_transform, u, method='talbot')
