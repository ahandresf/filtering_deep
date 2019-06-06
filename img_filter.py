#!/bin/usr/env python
'''
Andres Felipe Alba Hernandez
Fermi National Accelerator Laboratory
email: ahandresf@gmail.com
Date: Summer 2019
'''
import scipy
from scipy import ndimage, misc, signal
import skimage
from skimage import img_as_ubyte
import numpy as np
import matplotlib.image as mpimg #image reader
import matplotlib.pyplot as plt
import matplotlib.cm as cm #colors
from filter_conf import CURRENT_DIR, DATA_DIR, OUTPUT_DIR

#file name
#input_file='obj_ra120.05441848_dec8.20232396'
input_file='output_notebook.npy'
output_file=OUTPUT_DIR+input_file.split('.npy')[0]+'_fil.npy'
print('input_file:',input_file)
print('output_file: ',output_file)

#getting image
image_file=DATA_DIR+'/'+input_file
#img = mpimg.imread(image_file)
img=np.load(image_file)

#you should use float 32 or something better or you will get NaN values.
fil_sig=signal.wiener(img.astype('float64'), mysize=None, noise=None) #filter signal

#Normalizing and convertin to unsigned integer of eight digits
fil_sig=255*(fil_sig-fil_sig.min())/(fil_sig.max()-fil_sig.min())
fil_sig=fil_sig.round()
fil_sig=fil_sig.astype(np.uint8)
np.save(output_file,fil_sig)
print('Storing image at: %s'%output_file)

'''
fig_t, axs_t = plt.subplots(1,2)
axs_t[0].imshow(img)
axs_t[1].imshow(fil_sig)
plt.show()
'''
#plt.imshow(fil_sig)
#plt.savefig('image.jpg')
