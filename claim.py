import random

import numpy as np

THRESHOLD = 0.3


# Will draw a sample from X_i claims distribution.
def generate_claim():
    p = random.random()
    U = np.random.uniform
    return U(0, 1) if p <= THRESHOLD else U(2, 4)
