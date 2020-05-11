import matplotlib.pyplot as plt
import numpy as np
field = ['lin(R = 2.5km)', 'lin(R = 1.5km)', 'lin(R = 0.5km)',
         'exp(R = 2.5km)', 'exp(R = 1.5km)', 'exp(R = 0.5km)',
         'even(R = 2.5km)', 'even(R = 1.5km)', 'even(R = 0.5km)',
         'rand(R = 2.5km)', 'rand(R = 1.5km)', 'rand(R = 0.5km)',
         'c_even(R = 2.5km)', 'c_even(R = 1.5km)', 'c_even(R = 0.5km)',
         'c_grad(R = 2.5km)', 'c_grad(R = 1.5km)', 'c_grad(R = 0.5km)',
         'c_ring(R = 2.5km)', 'c_ring(R = 1.5km)', 'c_ring(R = 0.5km)']

#---------------------------------------------
#   PROBABILITY FIELD (3 SIZES AND 3 SHAPES)
#---------------------------------------------
#   Three Field Size.
linesize = [126, 76, 26] # Accordingly, the diameter is 250*20(5km), 150*20(3km), 50*20(1km)
savepath = 'D:/geoscience/MScResearch/shape10/'
#   shape 1: linear
shape1 = np.zeros((3,251,251))
line = np.zeros((3, 126))
line[0][:126] = range(126, 0, -1)#   Large Field
line[1][:76] = range(76, 0, -1)#   Medium Field
line[2][:26] = range(26, 0, -1)#   Small Field
for size in range(3):
    for row in range(251): #from 0 to 250
        for col in range(251):
            idx = max(abs(row + 1 - 126), abs(col + 1 - 126))
            if idx < linesize[size]:
                shape1[size][row][col] = line[size][idx]
    shapesum = np.sum(shape1[size])
    shape1[size] = shape1[size] / shapesum
plt.imshow(shape1[2], cmap='Blues')
#           interpolation="nearest", origin="upper")
plt.colorbar()
plt.show()
for size in range(3):
    np.savetxt(savepath+ str(size)+ 'shape1.asc',shape1[size])



#   shape 2: near-exponential
import math
shape2 = np.zeros((3,251,251))
line = np.zeros((3, 126))
for i in range(0, 126):
    line[0][i] = math.e**(-i)#   Large Field
for i in range(0, 76):
    line[1][i] = math.e**(-i)#   Medium Field
for i in range(0, 26):
    line[2][i] = math.e**(-i)#   Small Field
for size in range(3):
    for row in range(251): #from 0 to 250
        for col in range(251):
            idx = max(abs(row + 1 - 126), abs(col + 1 - 126))
            if idx < linesize[size]:
                shape2[size][row][col] = line[size][idx]
    shapesum = np.sum(shape2[size])
    shape2[size] = shape2[size] / shapesum
plt.imshow(shape2[0], cmap='Blues')
#           interpolation="nearest", origin="upper")
plt.colorbar()
plt.show()
for size in range(3):
    np.savetxt(savepath+ str(size)+ 'shape2.asc',shape2[size])



#   shape 3: even
shape3 = np.zeros((3,251,251))
shape3[0] = 1/(251*251)
shape3[1][50:201,50:201] = 1/(76*76)
shape3[2][100:151,100:151] = 1/51/51
for size in range(3):
    np.savetxt(savepath+ str(size)+ 'shape3.asc',shape3[size])
plt.imshow(shape3[2], cmap='Blues')
#           interpolation="nearest", origin="upper")
plt.colorbar()
plt.show()

#   shape 4: no-shape/ random
shape4 = np.zeros((3,251,251))
import random as rd
for row in range(251):
    for col in range(251):
        shape4[0][row, col] = rd.randint(0, 100) * 0.01
for row in range(50, 201):
    for col in range(50,201):
        shape4[1][row, col] = rd.randint(0, 100) * 0.01
for row in range(100, 151):
    for col in range(100, 151):
        shape4[2][row, col] = rd.randint(0, 100) * 0.01
for size in range(3):
    shapesum = np.sum(shape4[size])
    shape4[size] = shape4[size] / shapesum
for size in range(3):
    np.savetxt(savepath+ str(size)+ 'shape4.asc',shape4[size])
plt.imshow(shape4[2], cmap='Blues')
#           interpolation="nearest", origin="upper")
plt.colorbar()
plt.show()

#   shape 5
    # The center pixel has a probability of 60%, the rest have the same probability and adds up to 40%.
shape5 = np.zeros((3,251,251))
shape5[0] = 0.4/(251*251-1)
shape5[1][50:201,50:201] = 0.4/(151*151-1)
shape5[2][100:151,100:151] = 0.4/(51*51-1)
shape5[0][125, 125] = 0.6
shape5[1][125, 125] = 0.6
shape5[2][125, 125] = 0.6 
for size in range(3):
    np.savetxt(savepath+ str(size)+ 'shape5.asc',shape5[size])
plt.imshow(shape5[0], cmap='Blues')
#           interpolation="nearest", origin="upper")
plt.colorbar()
plt.show()

#   shape 6
    # The center pixel has a probability of 60%, the rest have the same probability and adds up to 40%.
    # This shape differs from shape 5 in the way that each ring has an equal total probability.
    # While shape 5 has different total probability for each ring.
shape6 = np.zeros((3,251,251))
ring = [125, 75, 25]
for size in range(3):
    ringprob = 0.4/ring[size]
    for row in range(125 - ring[size], 126 + ring[size]):
        for col in range(125 - ring[size], 126 + ring[size]):
            pixels = 8*max(abs(row - 125), abs(col - 125)) 
            if pixels != 0:
                shape6[size][row][col] = ringprob/pixels
shape6[0][125, 125] = 0.6
shape6[1][125, 125] = 0.6
shape6[2][125, 125] = 0.6 
for size in range(3):
    np.savetxt(savepath+ str(size)+ 'shape6.asc',shape6[size])
#   shape 7
    # The center pixel has a probability of 60%, the rest have the same probability and adds up to 40%.
    # This shape has larger rings.
shape7 = np.zeros((3,251,251))
ringprob = 0.4
    #   large size
ring0 = [[0, 250], [25, 225], [50, 200], [75, 175], [100, 150], [125, 125]]
ring0prob = ringprob/5
# Calculate the probability for each pixel inside each ring
for ringnum in range(5):
    pixel = (ring0[ringnum][1] - ring0[ringnum][0] + 1)**2 - (ring0[ringnum + 1][1] - ring0[ringnum + 1][0] + 1)**2
    prob = ring0prob / pixel
    shape7[0][ring0[ringnum][0]:ring0[ringnum][1], ring0[ringnum][0]:ring0[ringnum][1]] = prob
    #   Medium size
ring1 = [[0, 150],[25, 125],[50, 100], [75, 75]]
ring1prob = ringprob/5
# Calculate the probability for each pixel inside each ring
for ringnum in range(3):
    pixel = (ring1[ringnum][1] - ring1[ringnum][0] + 1)**2 - (ring1[ringnum + 1][1] - ring1[ringnum + 1][0] + 1)**2
    prob = ring1prob / pixel
    shape7[1][ring1[ringnum][0] + 50 : ring1[ringnum][1] + 50, ring1[ringnum][0] + 50 : ring1[ringnum][1] + 50] = prob
    #   Small size
ring2 = [[0, 50], [25, 25]]
ring2prob = ringprob
# Calculate the probability for each pixel inside each ring
for ringnum in range(1):
    pixel = (ring2[ringnum][1] - ring2[ringnum][0] + 1)**2 - (ring2[ringnum + 1][1] - ring2[ringnum + 1][0] + 1)**2
    prob = ring2prob / pixel
    shape7[2][ring2[ringnum][0] + 100 : ring2[ringnum][1] +100, ring2[ringnum][0] + 100 :ring2[ringnum][1] + 100] = prob
shape7[0][125, 125] = 0.6
shape7[1][125, 125] = 0.6
shape7[2][125, 125] = 0.6 
for size in range(3):
    np.savetxt(savepath+ str(size)+ 'shape7.asc',shape7[size])

#
#   Possible values are: Accent, Accent_r, Blues, Blues_r, BrBG, BrBG_r, BuGn, BuGn_r, BuPu, BuPu_r, CMRmap, CMRmap_r, Dark2, Dark2_r, GnBu, GnBu_r, Greens, Greens_r, Greys, Greys_r, OrRd, OrRd_r, Oranges, Oranges_r, PRGn, PRGn_r, Paired, Paired_r, Pastel1, Pastel1_r, Pastel2, Pastel2_r, PiYG, PiYG_r, PuBu, PuBuGn, PuBuGn_r, PuBu_r, PuOr, PuOr_r, PuRd, PuRd_r, Purples, Purples_r, RdBu, RdBu_r, RdGy, RdGy_r, RdPu, RdPu_r, RdYlBu, RdYlBu_r, RdYlGn, RdYlGn_r, Reds, Reds_r, Set1, Set1_r, Set2, Set2_r, Set3, Set3_r, Spectral, Spectral_r, Wistia, Wistia_r, YlGn, YlGnBu, YlGnBu_r, YlGn_r, YlOrBr, YlOrBr_r, YlOrRd, YlOrRd_r, afmhot, afmhot_r, autumn, autumn_r, binary, binary_r, bone, bone_r, brg, brg_r, bwr, bwr_r, cividis, cividis_r, cool, cool_r, coolwarm, coolwarm_r, copper, copper_r, cubehelix, cubehelix_r, flag, flag_r, gist_earth, gist_earth_r, gist_gray, gist_gray_r, gist_heat, gist_heat_r, gist_ncar, gist_ncar_r, gist_rainbow, gist_rainbow_r, gist_stern, gist_stern_r, gist_yarg, gist_yarg_r, gnuplot, gnuplot2, gnuplot2_r, gnuplot_r, gray, gray_r, hot, hot_r, hsv, hsv_r, inferno, inferno_r, jet, jet_r, magma, magma_r, nipy_spectral, nipy_spectral_r, ocean, ocean_r, pink, pink_r, plasma, plasma_r, prism, prism_r, rainbow, rainbow_r, seismic, seismic_r, spring, spring_r, summer, summer_r, tab10, tab10_r, tab20, tab20_r, tab20b, tab20b_r, tab20c, tab20c_r, terrain, terrain_r, twilight, twilight_r, twilight_shifted, twilight_shifted_r, viridis, viridis_r, winter, winter_r    