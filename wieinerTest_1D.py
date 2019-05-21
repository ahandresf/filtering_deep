#!/bin/usr/env python
import scipy
from scipy import ndimage, misc, signal
import numpy as np
import matplotlib.pyplot as plt

#time
start = -2*np.pi #start sin(wt)
stop = 2*np.pi #end sin(wt)
t=np.linspace(start, stop, num=500, endpoint=True, retstep=False, dtype=None, axis=0)

#Noise
np.random.seed(19680801)
sigma=0.1
mu=0
nse = sigma*np.random.randn(len(t))+mu # white noise

#pure signal
hf=np.sin(t) #low frequency sin(wt)
lf=np.sin(1000*t) #high frequency sin(1000*wt)
sig=hf+lf #signal

#adding noise
sig_nse = sig + nse #signal + noise

#filter signal
fil_sig=signal.wiener(sig_nse, mysize=None, noise=None) #filter signal

fig, axs = plt.subplots(3,1)
axs[0].plot(t,sig_nse)
axs[0].set_xlabel('Angle [rad] in time domain')
axs[0].set_ylabel('Signal+Noise')

axs[1].plot(t,fil_sig)
axs[1].set_xlabel('Angle [rad] in time domain')
axs[1].set_ylabel('filter(signal+noise)')

axs[2].plot(t,sig)
axs[2].set_xlabel('Angle [rad] in time domain')
axs[2].set_ylabel('Original Signal')
plt.show()
