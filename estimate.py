import numpy as np
import matplotlib.pyplot as plt

from claim import generate_itd_claim


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
    print('Ruined = {:.4f}%'.format(bankrupt_percent))


def advanced_monte_carlo(model, examples=10):
    probabilities_sum = 0

    for i in range(examples):

        p = 1 - (model.rate * model.mu) / model.c

        G = np.random.geometric(p)

        itd_claims_sum = 0
        for _ in range(G):
            itd_claims_sum += generate_itd_claim()

        if model.u_initial >= itd_claims_sum:
            probabilities_sum += 1

        print(f'{i} / {examples}')

    ruin_probability = probabilities_sum / examples
    print('Ruin = {:.4f} %'.format(ruin_probability))



