import time

from estimate import basic_monte_carlo, advanced_monte_carlo
from insurance import Model
from plot import plot_trajectories


short_model = Model(u_initial=1, c=4.5, rate=1, mu=2.25, t_end=5)
long_model = Model(u_initial=1, c=4.5, rate=1, mu=2.25, t_end=1000)

# plot_trajectories(short_model)


# t = time.time()
# basic_monte_carlo(long_model, examples=1000)
# elapsed = time.time() - t
#
# print('Time Elapsed = ', elapsed, 's')


t = time.time()
advanced_monte_carlo(long_model, examples=100000)
elapsed = time.time() - t

print('Time Elapsed = ', elapsed, 's')


