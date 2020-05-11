import os.path, sys
import numpy as np
import pandas as pd
from numpy import array
import matplotlib.pyplot as plt
from scipy import stats
#---------------------------------------------
#   Regression between Model Result and Reference
#---------------------------------------------

refpath = "D:/geoscience/MScResearch/Analysis0930/reference.asc"
refExpo = np.loadtxt(refpath, skiprows =6)
#--------------------------------------------------------------Regression for one file
myresult = np.zeros((645, 771))
allx = np.zeros((36739)) # allx: the model result in one row
resultpath = "D:/geoscience/MScResearch/Analysis0930/exWithoutRoad/size0shape1.asc"      
mresult = np.loadtxt(resultpath, skiprows = 6)            
for row in range(645):
    for col in range(771):
        if refExpo[row][col] == -9999:
            mresult[row][col] = -9999
        if mresult[row][col] == 0:
            refExpo[row][col] = 0
myresult = mresult
y = np.reshape(refExpo, (771*645))
x = np.reshape(myresult, (771*645))
x2 = []
# Take out the pixels with no value.
for xitem in x:
    if xitem != -9999 and xitem != 0:
        x2.append(xitem)
allx = x2
y2 = []
for yitem in y:
    if yitem != -9999 and yitem != 0:
        y2.append(yitem)        
slope, intercept, r_value, p_value, std_err = stats.linregress(x2, y2)
print("slope: %f    intercept: %f" % (slope, intercept))
print("r-squared: %f" % r_value**2)
#plt.plot(array(x2), array(y2), 'o', label='original data')
#plt.plot(array(x2), array(x2), '-', label = 'y = x ')
#plt.plot(array(x2), array(np.array(x2)+2),'-')
#plt.plot(array(x2), array(np.array(x2)-2),'-')
# Add title and axis names
plt.title('My title')
plt.xlabel('Commuter\'s exposure')
plt.ylabel('')
#--------------------------------------------------------------Regression for the folder
field:['linear (R:2.5km)', 'linear (R:1.5km)', 'linear (R:0.5km)',
         'exponential (R:2.5km)', 'exponential (R:1.5km)', 'exponential (R:0.5km)',
         'even (R:2.5km)', 'even (R:1.5km)', 'even (R:0.5km)',
         'random (R:2.5km)', 'random (R:1.5km)', 'random (R:0.5km)',
         'c_even (R:2.5km)', 'c_even (R:1.5km)', 'c_even (R:0.5km)',
         'c_thickRing (R:2.5km)', 'c_thickRing (R:1.5km)', 'c_thickRing (R:0.5km)',
         'c_narrowRing (R:2.5km)', 'c_narrowRing (R:1.5km)', 'c_narrowRing (R:0.5km)']
path = "D:/geoscience/MScResearch/Analysis0930/exWithoutRoad"
files = os.listdir(path)
allr = []
myresult = np.zeros(( 645, 771))
allx = np.zeros((36739)) # allx: the model result in one row
for file in files: 
    if file.endswith('asc') ==False:
        continue
    resultpath = 'D:/geoscience/MScResearch/Analysis0930/exWithoutRoad/' +file     
    mresult = np.loadtxt(resultpath, skiprows = 6)            
    for row in range(645):
        for col in range(771):
            if refExpo[row][col] == -9999:
                mresult[row][col] = -9999
            if mresult[row][col] == 0:
                refExpo[row][col] = 0
    myresult = mresult
    y = np.reshape(refExpo, (771*645))
    x = np.reshape(myresult, (771*645))
    x2 = []
    # Take out the pixels with no value.
    for xitem in x:
        if xitem != -9999 and xitem != 0:
            x2.append(xitem)
    allx = x2
    y2 = []
    for yitem in y:
        if yitem != -9999 and yitem != 0:
            y2.append(yitem)        
    slope, intercept, r_value, p_value, std_err = stats.linregress(x2, y2)
    allr.append([file, r_value])
    print("slope: %f    intercept: %f" % (slope, intercept))
    print("r-squared: %f" % r_value**2)
    plt.figure(figsize=(9,12))
    plt.plot(array(x2), array(y2), 'o', label='original data')
    plt.plot(array(x2), array(x2), '-', label = 'y = x ')
    #plt.plot(array(x2), array(np.array(x2)+2),'-')
    #plt.plot(array(x2), array(np.array(x2)-2),'-')
    # Add title and axis names
    shape = int(file[10])
    size = int(file[4])
    name = field[shape *3 - 3 + size]
    plt.title('Exposure Comparison (unit: μg/m3)'.format(name), fontsize = 20)
    plt.xlabel('Commuter\'s Exposure', fontsize = 16)
    plt.ylabel('{0}'.format(name), fontsize = 16)
    plt.savefig('D:/geoscience/MScResearch/Analysis0930/plotScatter/{0}.png'.format(file[:-4]))
# I used this!
#np.savetxt('D:/geoscience/MScResearch/Analysis0930/rsquared.txt', np.array([allr[0], allr[1]]))