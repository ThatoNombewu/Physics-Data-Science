import numpy as np
from matplotlib import pyplot as plt


Channels = np.array([166, 213 ,414 ,270],)
Energy = np.array([511, 661.657, 1274.54, 834.848])


m, c = np.polyfit( Channels, Energy,1)

print('The best fit equation is :','y = ',m,'x + ',c)

fit = Channels*m + c

plt.scatter(Channels,Energy)
plt.plot(Channels, fit)
plt.show()
