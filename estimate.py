import numpy as np
from claim import generate_itd_claim
from insurance import Model


# Generates trajectories and computes the ruin probability experimentally.
def basic_monte_carlo(model: Model, examples: int = 10) -> float:
    T = np.arange(model.t_start, model.t_end, 0.01)
    U = np.vectorize(model.U)

    share_of_ruins = 0
    for i in range(examples):
        if np.any(U(T) < 0):
            share_of_ruins += 1
        model.refresh()

    ruined_percent = share_of_ruins / examples * 100
    print('Ruined = {:.4f}%'.format(ruined_percent))
    return ruined_percent


# Computes ruin probability based on geometric amount of
# integrated tail distribution random variables.
def advanced_monte_carlo(model: Model, examples: int = 10) -> float:
    share_of_ruins = 0
    for i in range(examples):
        p = 1 - (model.rate * model.mu) / model.c
        G = np.random.geometric(p) - 1

        itd_claims_sum = 0
        for _ in range(G):
            itd_claims_sum += generate_itd_claim()

        if model.u_initial < itd_claims_sum:
            share_of_ruins += 1

    ruined_percent = share_of_ruins / examples * 100
    print('Ruined = {:.4f} %'.format(ruined_percent))
    return ruined_percent
