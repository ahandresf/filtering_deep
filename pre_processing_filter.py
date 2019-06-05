#!/bin/usr/env python
import scipy
from scipy import ndimage, misc, signal
import skimage
import numpy as np
import matplotlib.image as mpimg #image reader
import matplotlib.pyplot as plt
import matplotlib.cm as cm #colors



#We have two main sources of data sets
#CASSOWARY https://www.ast.cam.ac.uk/ioa/research/cassowary/
#SDSS Quasar Lens Search (SQLS) http://www-utap.phys.s.u-tokyo.ac.jp/~sdss/sqls/lens.html
#dropbox_dataset: https://www.dropbox.com/sh/uuvacgaukfe7jo9/AAC8tvf5KptrHalLasbUfjE0a?dl=0

data_dir='/home/leasanspy/Dropbox/RA_Fermilab/Lenses_DataSet/CASSOWARY/cassowary_download/' #location of data
#getting image
file_name='obj_ra120.05441848_dec8.20232396'
image_file=data_dir+file_name
img = mpimg.imread(image_file)


# Convert the image taking each channel
R = img[:, :, 0] #red
G = img[:, :, 1] #green
B = img[:, :, 2] #blue

#Filter the signal and plot
fil_sig=signal.wiener(R.astype('float32'), mysize=None, noise=None) #filter signal
fig_t, axs_t = plt.subplots(1,2)
axs_t[0].imshow(img)
axs_t[1].imshow(fil_sig)



#fourier transform
#sig_f=scipy.fftpack.fft2(sig) #signal in frequency domain
