import random
import numpy as np


def generate_claim():
    p = random.random()
    return 1 if p <= .5 else 10


def generate_itd_claim():
    xi = np.random.uniform(0, 1)

    if xi < 0.1818182:
        return (11*xi)/2
    else:
        return 11*xi - 1
