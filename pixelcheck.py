import os, sys, inspect
import dupecheck
import random
from random import randint

from PIL import Image   #I am using Pillow! pip install pillow
import sizesort
import check #A intchecker if the input data is ACTUALLY integer


def pixelmain(name1,name2):
    print('pixelmain here')

    index =0
    pic1 = Image.open(name1)
    pic2= Image.open(name2)

    width, height = pic1.size
    samplesize = 50 #pixels
    same=0
    diff=0
    idnex=0
    for index in range(0,samplesize):
        randwidth=randint(0,width)
        randheight=randint(0,height)
        rgb_val1 = pic1.convert('RGB')
        r1, g1, b1 = pic1.getpixel((randwidth,randheight))
        #print("==========")
        #print("testing"+str(randwidth)+" "+str(randheight))
        #print("values: " +str(r1) +" "+ str(g1) + " "+str(b1))

        rgb_val2 = pic2.convert("RGB")
        r2, g2, b2 = pic2.getpixel((randwidth,randheight))
        #print("testing"+str(randwidth)+" "+str(randheight))
        #print("values: " +str(r2) +" "+ str(g2) + " "+str(b2))
        #print("=========")

        if r1 == r2 and g1 == g2 and b1 ==b2 :
            same +=1
            print('they are the same')
        else :
            diff +=1
            print('they differentiate')


    returnval= (same / samplesize)*100
    return returnval
