import numpy as np
import matplotlib.pyplot as plt
road = np.loadtxt('D:/geoscience/MScResearch/Analysis0930/roadUtrecht.asc',
                    ndmin = 1, skiprows = 6)
cc = np.loadtxt('D:/geoscience/MScResearch/FourSeasonsH/s4mean20.asc', 
                 ndmin = 1, skiprows = 6)
noroad = np.zeros((645, 771))
for row in range(645):
    for col in range(771):
        if road[row][col] != 0:
            noroad[row][col] = 0
        else:
            noroad[row][col] = cc[row][col]

np.savetxt('D:/geoscience/MScResearch/Analysis0930/s4mean20noroad.asc', noroad)

#
plt.imshow(cc, cmap='Blues')
plt.colorbar()
plt.show()