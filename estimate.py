import numpy as np
import matplotlib.pyplot as plt


def basic_monte_carlo(model, examples=10):

    T = np.arange(model.t_start, model.t_end, 0.01)
    U = np.vectorize(model.U)

    share_of_bankrupts = 0
    for i in range(examples):

        if np.any(U(T) < 0):
            share_of_bankrupts += 1
        model.refresh()

        if i % 20 == 0:
            print(f'{i+1} / {examples}')
            print('Current ruined percent = {:.2f}%'.format(share_of_bankrupts / (i + 1) * 100))

    bankrupt_percent = share_of_bankrupts / examples * 100
    print('Finished')
    print('Ruined = {:.2f}%'.format(bankrupt_percent))

