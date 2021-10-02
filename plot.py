import matplotlib.pyplot as plt
import numpy as np


def plot_trajectories(model, filename):
    T = np.arange(model.t_start, model.t_end, 0.001)
    U = np.vectorize(model.U)

    plt.clf()

    for _ in range(5):
        plt.plot(T, U(T))
        model.refresh()

    plt.xlabel('t')
    plt.ylabel('U(t)')

    plt.savefig(filename)



