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
#location of data
#DATA_DIR='/home/leasanspy/Dropbox/RA_Fermilab/Lenses_DataSet/CASSOWARY/cassowary_download/'
DATA_DIR=CURRENT_DIR
#DATA_DIR=CURRENT_DIR+'/data/'
OUTPUT_DIR=CURRENT_DIR+'/Output_Filter/'
os.makedirs(OUTPUT_DIR, exist_ok=True)
