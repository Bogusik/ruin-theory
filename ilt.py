from mpmath import *

mp.dps = 4
mp.pretty = True


def get_ilt_first(t):
    f_p = lambda p: (1 - (1 * 2.25 / 4.5)) / (
            p * (1 - (1 / 4.5) *
                 (0.35 * exp(-4 * p) / (p ** 2) - 0.35 * exp(-2 * p) / (
                         p ** 2) + 0.3 * exp(-p) / (p ** 2) - 0.3 / (
                          p ** 2) + 1 / p)
                 ))
    return invertlaplace(f_p, t, method='talbot')


def get_ilt_second(t):
    f_p = lambda p: (1 - (5 * 2.25 / 11.8125)) / (
            p * (1 - (5 / 11.8125) *
                 (0.35 * exp(-4 * p) / (p ** 2) - 0.35 * exp(-2 * p) / (
                         p ** 2) + 0.3 * exp(-p) / (p ** 2) - 0.3 / (
                          p ** 2) + 1 / p)
                 ))
    return invertlaplace(f_p, t, method='talbot')
