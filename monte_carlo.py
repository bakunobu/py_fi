from time import time
from math import exp, sqrt, log
from random import gauss, seed

'''
Base vars
=========
'''

seed(2000)
t0 = time()

'''
Params
======
'''

S0 = 100.0 # initial value
K = 105.0 # strike price
T = 1.0 # maturity
r = 0.05 # riskless short rate
sigma = 0.2 # volatility
M = 50 # number of time steps
dt = T / M # length of time interval
I = 250_000 # number of paths

# Simulating a path with M time steps
S = []
for i in range(I):
    path = []
    for t in range(M + 1):
        if t == 0:
            path.append(S0)
        else:
            z = gauss(0.0, 1.0)
            St = path[t - 1] * exp((r - 0.5 * sigma ** 2) * dt + sigma * sqrt(dt) * z)
            path.append(St)
    S.append(path)

# Calculating the Monte Carlo extimator
C0 = exp(-r * t) * sum([max(path[-1] - K, 0) for path in S]) / I

# Results output
tpy = time() - t0
print('European Option Value %7.3f' % C0)
print('Duration in Seconds %7.3f' % tpy)
