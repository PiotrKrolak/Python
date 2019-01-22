#
# https://matplotlib.org/tutorials/introductory/pyplot.html#sphx-glr-tutorials-introductory-pyplot-py

import numpy as np

# (od, do, probkowanie)
t = np.arange(0., 5., 0.2)

# czerwone(r) kreski(--), niebieskie(b) kwadraty(s) i zielone(g) trojkaty(^)
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')

plt.show()
