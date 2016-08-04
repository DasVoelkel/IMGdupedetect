from PIL import Image

import glob, os, sys

import random
comp = 1000

fixes=["*.jpg","*.png","*.jpeg","*.JPEG","*.PNG","*.JPEG"]

path = os.path.dirname(os.path.realpath(__file__))
path = path + "/pics"
os.chdir(path)
count =0

for fixmain in fixes:

    for name1 in glob.glob(fixmain):
        print(name1)
        count =count +1
        print (str(count))
