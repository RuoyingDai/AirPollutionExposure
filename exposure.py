import numpy as np
import matplotlib.pyplot as plt
c1 = np.loadtxt('D:/geoscience/MScResearch/Analysis0930/s4mean20.asc',
                ndmin = 1, skiprows = 6)
#   The exposure result set of c1 has been saved in Analysis0930/exWithRoad
c2 = np.loadtxt('D:/geoscience/MScResearch/Analysis0930/s4mean20noroad.asc')
#   The exposure result set of c2 has been saved in Analysis0930/exWithoutRoad 
plt.imshow(c2, cmap='Blues')
plt.colorbar()
plt.show()
#
ref = np.loadtxt('D:/geoscience/MScResearch/Analysis0930/reference.asc', 
                     ndmin = 1, skiprows = 6)# The null value is -9999
ex = np.zeros((645, 771))
header = "ncols     771\n" 
header += "nrows     645\n" 
header += "xllcorner 126432\n"
header += "yllcorner 448710\n"
header += "cellsize 20\n"
header += "NODATA_value 0" 
cc = c1
for shape in range(1, 8):
    for size in range(3):
        print('shape:{0}, size:{1}'.format(shape, size))
        path = 'D:/geoscience/MScResearch/Shape/{0}shape{1}.asc'.format(size, shape)
        field = np.loadtxt(path, ndmin = 1)
        for row in range(645):
            for col in range(771):
                if ref[row][col] != -9999:
                    no2 =  cc[row - 125:row + 126, col - 125:col + 126]
                    if np.isnan(no2).shape[0] != 251 or np.isnan(no2).shape[1] !=251 :
                        continue
                    time = np.multiply(no2, field)
                    kernel = np.sum(time)
                    prob = np.sum(field[no2 !=0])
                    ex[row][col] = kernel / prob *0.7
        np.savetxt('D:/geoscience/MScResearch/Analysis0930/exWithRoad/size{0}shape{1}.asc'.format(size, shape), 
                   ex, header = header, comments = '')  
        print('saved.')

plt.imshow(ex, cmap='Blues')
plt.colorbar()
plt.show()