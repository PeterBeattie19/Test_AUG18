from scipy.stats import *
import numpy as np
import matplotlib.pyplot as plt

data = np.random.randint(100, size = 100)
std = tstd(data)
data = list(map(lambda x: x/std, data)) 

plt.plot(data)
plt.show()