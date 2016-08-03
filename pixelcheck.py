import os, sys, inspect
import dupecheck
import random
from random import randint

from PIL import Image   #I am using Pillow! pip install pillow
import sizesort
import check #A intchecker if the input data is ACTUALLY integer


def pixelmain(name1,name2,samplesize):
    print('pixelmain here')

    index =0
    pic1 = name1
    pic2 = name2

    width, height = pic1.size
    samplesize = samplesize #pixels
    same=0
    diff=0
    pic1.convert('RGBA')
    pic2.convert('RGBA')

    usedwidth=[]
    usedheight=[]



    for index in range(0,samplesize):#minimalabstände voneinander von den pixen

        w=True
        h=True
        while w and h:
            w=False
            h=False

            randwidth=randint(0,width-1)# 0,0 pixel exsists. 1600 1600 not necessarily
            randheight=randint(0,height-1)

            for i in range(0,len(usedwidth)):
                if randwidth == usedwidth[i]:
                    w=True
                else:
                    w=False


            for i in range(0,len(usedheight)):
                if randheight == usedheight[i]:
                    h=True
                else:
                    h=False


        usedwidth.append(randwidth)
        usedheight.append(randheight)
        pixel1 = pic1.getpixel((randwidth,randheight))
        #print("==========")
        #print("testing"+str(randwidth)+" "+str(randheight))
        #print("values: " +str(r1) +" "+ str(g1) + " "+str(b1))


        pixel2 = pic2.getpixel((randwidth,randheight))

        #print("testing"+str(randwidth)+" "+str(randheight))
        #print("values: " +str(r2) +" "+ str(g2) + " "+str(b2))
        #print("=========")

        if pixel1 == pixel2:
            same +=1
            print('they are the same')
        else :
            diff +=1
            print('they differentiate')


    returnval= (same / samplesize)*100
    return returnval
