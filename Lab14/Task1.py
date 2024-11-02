import matplotlib.pyplot as plt  
import numpy as np

t = np.linspace(1, 8, 51) 

y = 5*np.sin(10*t)*np.sin(3*t)/(t**t)

plt.plot(t, y, label='5*sin(10t)*sin(3t)/(t^t)', color = "red", linewidth = 5)

plt.title('My plot, var 12', fontsize=15)   # назва графіка 

plt.xlabel('t', fontsize=12, color='blue') # позначення вісі абсцис
plt.ylabel('y', fontsize=12, color='blue') # позначення вісі ординат  
plt.legend()
plt.grid(True)

plt.show()  # відображення графіка
