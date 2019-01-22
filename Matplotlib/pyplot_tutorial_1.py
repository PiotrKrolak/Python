#
# https://matplotlib.org/tutorials/introductory/pyplot.html#sphx-glr-tutorials-introductory-pyplot-py

import matplotlib.pyplot as plt
import numpy as np

plt.plot([1,2,3,4]) # tu podaje "y" a "x" to bedzie liczba porzatkowa
plt.plot([0,1,2,3],[2,4,8,16]) # ([x0,x1,x2,..],[y0,y1,y2,..])
plt.plot([0,1,2,3],[4,8,16,32],'ro') # 'ro' argument ktory ryzaznacza wykres kropkami

plt.show()
