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
    xi = min(xi, 1156 / 1170)
    return 1 / 13 * (34 - np.sqrt(1170 - 1170 * xi))
