from scipy.stats import *
import numpy as np
import matplotlib.pyplot as plt

data = np.random.randint(100, size = 100)
print(tmean(data))
std = tstd(data)
print(std)
plt.plot(data)
plt.show()

data = list(map(lambda x: x/std, data)) 

print(tmean(data))
print(tstd(data)) 

plt.plot(data)
plt.show()