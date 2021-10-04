from poisson import generate_arrival_times, generate_claims, get_claims_sum


# A class that encapsulates insurance process U(t).
class Model:
    def __init__(self, u_initial: float, c: float, rate: float, mu: float,
                 t_end: float) -> None:
        self.u_initial = u_initial
        self.c = c
        self.rate = rate
        self.mu = mu
        self.t_start = 0
        self.t_end = t_end
        self.arrival_times = generate_arrival_times(self.rate, t_end=self.t_end)
        self.claims = generate_claims(self.arrival_times)

    # Returns the value of Insurance Process U(t).
    def U(self, t: float) -> float:
        return self.u_initial + self.c * t - get_claims_sum(t, self.claims,
                                                            self.arrival_times)

    # Generates new arrival times and claims.
    def refresh(self) -> None:
        self.arrival_times = generate_arrival_times(self.rate)
        self.claims = generate_claims(self.arrival_times)
