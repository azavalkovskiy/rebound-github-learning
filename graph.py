#!/usr/bin/env python

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
data = np.loadtxt("r.txt")
t = data[:,0]
r = data[:,1]
plt.plot(t,r)
plt.show()

