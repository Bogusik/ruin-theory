# ruin-theory
A small model implementing basic Cramér–Lundberg model (or classical compound-Poisson risk model, classical risk process or Poisson risk process)

### **Initialization**

Class `Model` describes all model-related features. Use `Model()` to create its instance.
```python
model = Model(u_initial=20, c=15.5, rate=3, mu=2.7, t_end=50)
```
`u_initial` - initial company capital.  
`c` - premium rate.  
`rate` - rate of insurance cases.  
`mu` - mean of insurance payments.  
`t_end` - upper bound of the time interval (lower is 0).

### **Trajectories**

Use `plot_trajectories` to visualize the risk process. Pass `Model` instance and `filename` as parameters.
```python
from plot import plot_trajectories
plot_trajectories(model, 'model_1.png')
```

### **Basic Monte Carlo**

Use `basic_monte_carlo` to compute the _RUIN_ probability using brute-force Monte Carlo method. Pass `Model` instance and `examples` amount as parameters.
```python
from estimate import basic_monte_carlo
ruin_probability = basic_monte_carlo(model, examples=100)
```

### **Advanced Monte Carlo**

Use `advanced_monte_carlo` to compute the _RUIN_ probability using integrated tail distribution. Pass `Model` instance and `examples` amount as parameters.
```python
from estimate import advanced_monte_carlo
ruin_probability = advanced_monte_carlo(model, examples=1000)
```

### **Inverse Laplace Transform**

Use `get_ilt_first` or `get_ilt_second` respectively to figure out the true _SURVIVAL_ probability, using the numeric approximation of the inverse Laplace transform. Pass `u` initial capital argument to pass to inverse transform.
```python
from ilt import get_ilt_first, get_ilt_second
survival_probability_first = get_ilt_first(10)
survival_probability_second = get_ilt_second(50)
```

### **Maths**
Preliminary mathematical derivations and justifications can be found in [here](Insurance.pdf). 
