import time

from ilt import get_ilt_first, get_ilt_second
from estimate import basic_monte_carlo, advanced_monte_carlo
from insurance import Model
from plot import plot_trajectories


short_model_first = Model(u_initial=1, c=4.5, rate=1, mu=2.25, t_end=5)
long_model_first = Model(u_initial=1, c=4.5, rate=1, mu=2.25, t_end=1000)

# plot_trajectories(short_model_first, 'model_1.png')


# t = time.time()
# basic_monte_carlo(long_model_first, examples=1000)
# elapsed = time.time() - t
#
# print('Time Elapsed = ', elapsed, 's')
#
#
# t = time.time()
# advanced_monte_carlo(long_model_first, examples=1000)
# elapsed = time.time() - t
#
# print('Time Elapsed = ', elapsed, 's')


short_model_second = Model(u_initial=10, c=11.8125, rate=5, mu=2.25, t_end=5)
long_model_second = Model(u_initial=10, c=11.8125, rate=5, mu=2.25, t_end=10)

# plot_trajectories(short_model_second, 'model_2.png')

# t = time.time()
# basic_monte_carlo(long_model_second, examples=500)
# elapsed = time.time() - t
#
# print('Time Elapsed = ', elapsed, 's')


# t = time.time()
# advanced_monte_carlo(long_model_second, examples=1000)
# elapsed = time.time() - t
#
# print('Time Elapsed = ', elapsed, 's')


print("ILT {Ф(p)} (1) _I_ = ", get_ilt_first(1) * 100, '%')
print("ILT {Ф(p)} (10) _II_ = ", get_ilt_second(10) * 100, '%')

