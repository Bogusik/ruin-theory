import random

import numpy as np

THRESHOLD = 0.3


# Will draw a sample from X_i claims distribution.
def generate_claim():
    p = random.random()
    U = np.random.uniform
    return U(0, 1) if p <= THRESHOLD else U(2, 4)


# Will draw a sample from ~X_i integrated tail claim distribution.
def generate_itd_claim():
    xi = np.random.uniform(0, 1)

    if xi < 0.377777774:
        return 1 / 3 * (10 - np.sqrt(5) * np.sqrt(20 - 27 * xi))
    elif xi < 0.68888888:
        return (xi - 0.0666667) / 0.311111
    else:
        return 1 / 39 * (155 - np.sqrt(5) * np.sqrt(3900 - 3900 * xi))
