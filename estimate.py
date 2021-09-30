import numpy as np
import matplotlib.pyplot as plt


def basic_monte_carlo(model, examples=10):

    T = np.arange(model.t_start, model.t_end, 0.001)
    U = np.vectorize(model.U)

    share_of_bankrupts = 0
    for _ in range(examples):

        if np.any(U(T) < 0):
            share_of_bankrupts += 1
        model.refresh()

    bankrupt_percent = share_of_bankrupts / examples * 100
    print('Broke = {:.2f} %'.format(bankrupt_percent))

