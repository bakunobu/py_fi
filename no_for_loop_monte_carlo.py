import math
import numpy as np
from time import time


np.random.seed(2000)
t0 = time()


'''
Params
======
'''

S0 = 100.0
K = 105.0
T = 1.0
r = 0.05
sigma = 0.2
M = 50
dt = T / M
I = 250_000


'''
Simulation
==========
'''

S = S0 * np.exp(np.cumsum((r - 0.5 * sigma ** 2) * dt 
    + sigma * math.sqrt(dt) * np.random.standard_normal((M + 1, I)),
    axis = 0))

S[0] = S0
C0 = math.exp(-r * T) * sum(np.maximum(S[-1] - K, 0)) / I

tnp2 = time() - t0
print('European Option Value %7.3f' % C0)
print('Duration in Seconds %7.3f' % tnp2)
