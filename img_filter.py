#!/bin/usr/env python
'''
Andres Felipe Alba Hernandez
Fermi National Accelerator Laboratory
Northern Illinois University
email: ahandresf@gmail.com
Date: Summer 2019
'''
import sys
import os
import scipy
from scipy import ndimage, misc, signal
import skimage
from skimage import img_as_ubyte
import numpy as np
import matplotlib.image as mpimg #image reader
import matplotlib.pyplot as plt
import matplotlib.cm as cm #colors

CURRENT_DIR=os.getcwd()
#location of data
DATA_DIR='/home/leasanspy/Dropbox/RA_Fermilab/Lenses_DataSet/CASSOWARY/cassowary_download/'
#DATA_DIR=CURRENT_DIR+'/data/'
#getting image
file_name='obj_ra120.05441848_dec8.20232396'
image_file=DATA_DIR+file_name
img = mpimg.imread(image_file)

#you should use float 32 or something better or you will get NaN values.
fil_sig=signal.wiener(img.astype('float64'), mysize=None, noise=None) #filter signal

#Normalizing and convertin to unsigned integer of eight digits
fil_sig=255*(fil_sig-fil_sig.min())/(fil_sig.max()-fil_sig.min())
fil_sig=fil_sig.round()
fil_sig=fil_sig.astype(np.uint8)

fig_t, axs_t = plt.subplots(1,2)
axs_t[0].imshow(img)
axs_t[1].imshow(fil_sig)
