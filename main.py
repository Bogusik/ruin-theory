from ilt import get_ilt_first, get_ilt_second
from estimate import basic_monte_carlo, advanced_monte_carlo
from insurance import Model
from plot import plot_trajectories

# Declare model objects for the CASE 1.
short_model_first = Model(u_initial=1, c=4.5, rate=1, mu=2.25, t_end=10)
long_model_first = Model(u_initial=1, c=4.5, rate=1, mu=2.25, t_end=1000)

plot_trajectories(short_model_first, 'model_1.png')
basic_monte_carlo(long_model_first, examples=10)
advanced_monte_carlo(long_model_first, examples=100000)
print("1 - ILT_I {Ф(p)} (1) = ", (1 - get_ilt_first(1)) * 100, '%')

# Declare model objects for the CASE 2.
short_model_second = Model(u_initial=10, c=11.8125, rate=5, mu=2.25, t_end=10)
long_model_second = Model(u_initial=10, c=11.8125, rate=5, mu=2.25, t_end=1000)

plot_trajectories(short_model_second, 'model_2.png')
basic_monte_carlo(long_model_second, examples=10)
advanced_monte_carlo(long_model_second, examples=100000)
print("1 - ILT_II {Ф(p)} (10)  = ", (1 - get_ilt_second(10)) * 100, '%')
