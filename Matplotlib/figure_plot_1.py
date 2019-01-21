# documentation part 1
# Parts of a Figure

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()  # tworzy pusta figure
fig.suptitle('No axes on this figure')  # Dodanie nazwy(subtytulu)

fig, ax_lst = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes
plt.show()
