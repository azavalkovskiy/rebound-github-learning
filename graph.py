#!/usr/bin/env python

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#Plotting from a file printed in the format designated by reb_output_orbits
data = np.loadtxt("r.txt")
N = 5 # # of particles represented in array (tells how many rows to skip
#data is an array of format
# time[0], semimajor axis[1], eccentricity[2], inclination[3], Omega[4], omega[5], l[6], P[7], f[8]
t = data[::5,0]
var = data[::5,3]

plt.plot(t,var)
plt.show()

