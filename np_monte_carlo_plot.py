import math
import numpy as np
from time import time
import matplotlib.pyplot as plt


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

S = np.zeros((M + 1, I))
S[0] = S0
for t in range(1, M + 1):
    z = np.random.standard_normal(I)
    S[t] = S[t - 1] * np.exp((r - 0.5 * sigma ** 2)  * dt + sigma * math.sqrt(dt) * z)
    
C0 = math.exp(-r * T) * np.sum(np.maximum(S[-1] - K, 0)) / I

# plot
plt.plot(S[:, :10])
plt.grid(True)
plt.xlabel('time_step')
plt.ylabel('index_level')
plt.show()

#hist
plt.hist(S[-1], bins=50)
plt.grid(True)
plt.xlabel('index_level')
plt.ylabel('frequency')
plt.show()

#hist - sorted
plt.hist(np.maximum(S[-1] - K, 0), bins=50)
plt.grid(True)
plt.xlabel('option inner value')
plt.ylabel('frequency')
plt.ylim(0, 50000)

plt.show()