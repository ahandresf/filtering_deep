#!/bin/usr/env python
import scipy
from scipy import ndimage
import numpy as np
import math
import matplotlib.pyplot as plt

start = -2*np.pi #start sin(wt)
stop = 2*np.pi #end sin(wt)
x=np.linspace(start, stop, num=500, endpoint=True, retstep=False, dtype=None, axis=0)
hf=np.sin(x) #low frequency sin(wt)
lf=np.sin(1000*x) #high frequency sin(1000*wt)
y=hf+lf
plt.figure()
plt.plot(x,y)
plt.xlabel('Angle [rad] in time domain')
plt.ylabel('Signal with both components')
plt.show()
