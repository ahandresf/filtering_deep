#!/bin/usr/env python
import scipy
from scipy import ndimage, misc, signal
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


#getting image
image_file=('Lenna.png')
image = mpimg.imread(image_file)
#print("Image Shape:",image.shape())
plt.imshow(image)
#plt.show()
image.shape()

#Noise
np.random.seed(19680801)
sigma=0.1
mu=0
#nse = sigma*np.random.randn(len(t))+mu # white noise

#filter signal
#fil_sig=signal.wiener(sig_nse, mysize=None, noise=None) #filter signal

'''
fig, axs = plt.subplots(2,1)
axs[0].imshow(image)
axs[0].gray()
axs[0].title('Original Image')
plt.show()
'''
