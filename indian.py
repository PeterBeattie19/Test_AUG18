from scipy.stats import tstd, tmean
import numpy as np

data = np.random.randint(100, size = 100)
std = tstd(data)
mean = tmean(data) 

res = list(filter(lambda x: x > mean+std , data)) 
print(res) 