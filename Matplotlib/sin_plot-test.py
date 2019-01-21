#Rysowanie wykresu funkcji Sin(x)
#https://matplotlib.org/tutorials/introductory/usage.html#sphx-glr-tutorials-introductory-usage-py

import matplotlib.pyplot as plt
import numpy as np

#z = np.arange(0, 10, 0.2)
x = np.arange(0, 10, 0.2)
y = np.sin(x)
fig, ax = plt.subplots() # definiuje ax jako wykres
ax.plot(x, y) # przypisuje do wykresu "ax" pozycje x i y
plt.show() # wywoluje rysowanie wykresu
