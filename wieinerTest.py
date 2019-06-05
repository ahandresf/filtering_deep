#!/bin/usr/env python
import scipy
from scipy import ndimage, misc, signal
import skimage
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.cm as cm
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import LinearLocator, FormatStrFormatter


#import cv2

#getting image
image_file=('Lenna.png')
img = mpimg.imread(image_file)

# Convert the image taking each channel
R = img[:, :, 0] #red
G = img[:, :, 1] #green
B = img[:, :, 2] #blue
img_gray = R * 299. / 1000 + G * 587. / 1000 + B * 114. / 1000 #Gray image
#plt.imshow(img) #full color
#plt.imshow(img_gray,cmap=cm.gray)
#plt.show()

#signal
sig = R #for example pick the red channels

print("signal shape:",sig.shape)
#signal with noise
sig_nse=skimage.util.random_noise(sig, mode='gaussian', seed=None, clip=True)
#signal filtered
fil_sig=signal.wiener(sig_nse, mysize=None, noise=None) #filter signal

#fourier transform
sig_f=scipy.fftpack.fft2(sig) #signal in frequency domain
sig_nse_f=scipy.fftpack.fft2(sig_nse) #signal+noise in frequency domain
fil_sig_f=scipy.fftpack.fft2(fil_sig)
#plt.imshow(sig_nse)

#PLOTTING
#Space domain s and s+noise
fig_t, axs_t = plt.subplots(1,3)
axs_t[0].imshow(R,cmap=cm.gray)
axs_t[1].imshow(sig_nse,cmap=cm.gray)
axs_t[2].imshow(fil_sig,cmap=cm.gray)
#Fourier for s and s+noise
fig_f, axs_f = plt.subplots(1,3)
from matplotlib.colors import LogNorm
axs_f[0].imshow(abs(np.fft.fftshift(sig_f)),norm=LogNorm())
axs_f[1].imshow(abs(np.fft.fftshift(sig_nse_f)),norm=LogNorm())
axs_f[2].imshow(abs(np.fft.fftshift(fil_sig_f)), norm=LogNorm())

plt.show()


'''
X=np.arange(0,1,sig_f.shape[0])
Y=np.arange(0,1,sig_f.shape[1])
X, Y = np.meshgrid(X, Y)
Z=abs(np.fft.fftshift(sig_f))
fig = plt.figure()
ax = fig.gca(projection='3d')
# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
# Customize the z axis.
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)
'''
plt.show()


'''
#Noise
np.random.seed(19680801)
sigma=0.1
mu=0
nse = sigma*np.random.randn(sig.shape[0],sig.shape[1])+mu # white noise

fig, axs = plt.subplots(2,1)
axs[0].imshow(image)
axs[0].gray()
axs[0].title('Original Image')
plt.show()
'''
