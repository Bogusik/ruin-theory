import numpy as np
import matplotlib.pyplot as plt

from claim import generate_itd_claim


def basic_monte_carlo(model, examples=10):

    T = np.arange(model.t_start, model.t_end, 0.1)
    U = np.vectorize(model.U)

    share_of_ruins = 0
    for i in range(examples):

        if np.any(U(T) < 0):
            share_of_ruins += 1
        model.refresh()

        if i % 20 == 0:
            print(f'{i+1} / {examples}')
            print('Current ruined percent = {:.2f}%'.format(share_of_ruins / (i + 1) * 100))

    print('Finished')
    ruined_percent = share_of_ruins / examples * 100
    print('Ruined = {:.4f}%'.format(ruined_percent))


def advanced_monte_carlo(model, examples=10):
    share_of_ruins = 0

    for i in range(examples):

        p = 1 - (model.rate * model.mu) / model.c

        G = np.random.geometric(p) - 1

        itd_claims_sum = 0
        for _ in range(G):
            itd_claims_sum += generate_itd_claim()

        if model.u_initial < itd_claims_sum:
            share_of_ruins += 1

        if i % 20 == 0:
            print(f'{i+1} / {examples}')
            print('Current survival percent = {:.2f}%'.format(
                share_of_ruins / (i + 1) * 100))

    print('Finished')
    ruined_percent = share_of_ruins / examples * 100
    print('Ruined = {:.4f} %'.format(ruined_percent))



