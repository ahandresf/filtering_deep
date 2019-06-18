#!/bin/usr/env python
'''
Andres Felipe Alba Hernandez
Fermi National Accelerator Laboratory
email: ahandresf@gmail.com
Date: Summer 2019
'''
import sys
import os

CURRENT_DIR=os.getcwd()

##Location of data
#DATA_DIR='/lfstev/deepskies/lenses_bologna/ground'
DATA_DIR = '/data/ahandres'
#DATA_DIR=CURRENT_DIR
#DATA_DIR=CURRENT_DIR+'/data/'

##Input file name
INPUT_FILE='images.npy'

##Output
#OUTPUT_DIR=CURRENT_DIR+'/Output_Filter/'
OUTPUT_DIR=DATA_DIR+'/Output_Filter/'

#os.makedirs(OUTPUT_DIR, exist_ok=True) #Python3
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)
