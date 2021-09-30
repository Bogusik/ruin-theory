import matplotlib.pyplot as plt
import numpy as np


def plot_trajectories(model):
    T = np.arange(model.t_start, model.t_end, 0.001)
    U = np.vectorize(model.U)

    for _ in range(5):
        plt.plot(T, U(T))
        model.refresh()

    plt.savefig("trajectories.png")



