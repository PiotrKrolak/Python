#różne rodzaje wykresow na podwykresach
# https://matplotlib.org/tutorials/introductory/pyplot.html#sphx-glr-tutorials-introductory-pyplot-py

import matplotlib.pyplot as plt
import numpy as np

names = ['group_a', 'group_b', 'group_c'] # nazwy na osi x
values = [1, 10, 100] # wartosci na osi y

plt.figure(1, figsize=(9, 3)) # ???

plt.subplot(131) # na podwyrkesie 1 rzad trzy kolumny pierwszy wykres - 131
plt.bar(names, values) # wykres kolumnowy - bar
plt.subplot(132) # na podwyrkesie 1 rzad trzy kolumny drugi wykres - 132
plt.scatter(names, values) # wykres kropkowy - scatter
plt.subplot(133) # na podwyrkesie 1 rzad trzy kolumny trzeci wykres - 133
plt.plot(names, values) # wykres standardowy - plot
plt.suptitle('Categorical Plotting')

plt.show()
