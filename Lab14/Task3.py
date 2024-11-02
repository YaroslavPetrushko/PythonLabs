
import numpy as np

import matplotlib.pyplot as plt 

import sys

import os

x = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]

y = [70.265, 70.809, 70.944, 71.159, 71.186, 71.189, 71.476, 71.780, 71.582, 71.827]

print("Life expectancy at birth in Ukraine, total (years 2010-2019) ")

np.array(x)
np.array(y)
fig, ax = plt.subplots()
ax.pie(y, labels = x)
ax.axis("equal")
plt.legend() 
plt.show()