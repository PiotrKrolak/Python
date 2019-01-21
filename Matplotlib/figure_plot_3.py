# documentation part 3
# Parts of a Figure

import matplotlib.pyplot as plt
import numpy as np

# zdefiniowanie wlasnej funkcji do rysowania wykresow
def my_plotter(ax, data1, data2, param_dict):
    """
    A helper function to make a graph

    Parameters
    ----------
    ax : Axes
        The axes to draw to

    data1 : array
       The x data

    data2 : array
       The y data

    param_dict : dict
       Dictionary of kwargs to pass to ax.plot

    Returns
    -------
    out : list
        list of artists added
    """
    out = ax.plot(data1, data2, **param_dict)
    return out


data1, data2, data3, data4 = np.random.randn(4, 100) # wygenerowanie losowego zestawu danych
fig, ax = plt.subplots(1, 1) # dodanie pod wykresow 1 rzad 1 kolumna
my_plotter(ax, data1, data2, {'marker': 'x'}) # wywolanie wczesniej zdefiniowanej funkcji

plt.show() # wywolanie wykresow
