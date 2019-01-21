# documentation part 2
# Parts of a Figure

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2, 100)

# plt.plot(x, y, label='opis w legendzie wykresu')
plt.plot(x, x, label='linear')
plt.plot(x, x**2, label='quadratic')
plt.plot(x, x**3, label='cubic')

plt.xlabel('x label') # opis osi x
plt.ylabel('y label') # opis osi y 

plt.title("Simple Plot") # tytul wykresu

plt.legend() # wywolanie legendy wykresu

plt.show() # wywolanie wykresu
