import numexpr as ne
import numpy as np

a = np.arange(1, 1000)

ne.set_num_threads(4)
f = '3 * log(a) + cos(a) ** 2'
r = ne.evaluate(f)