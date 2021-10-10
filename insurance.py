from poisson import generate_arrival_times, generate_claims, get_claims_sum


class Model:
    def __init__(self, u_initial, c, rate, mu, t_end):
        self.u_initial = u_initial
        self.c = c
        self.rate = rate
        self.mu = mu
        self.t_start = 0
        self.t_end = t_end
        self.arrival_times = generate_arrival_times(self.rate, t_end=self.t_end)
        self.claims = generate_claims(self.arrival_times)

    def U(self, t):
        return self.u_initial + self.c * t - get_claims_sum(t, self.claims,
                                                            self.arrival_times)

    def refresh(self):
        self.arrival_times = generate_arrival_times(self.rate)
        self.claims = generate_claims(self.arrival_times)
