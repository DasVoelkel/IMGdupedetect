import os, sys, inspect
import dupecheck
import random
from random import randint

from PIL import Image   #I am using Pillow! pip install pillow
import sizesort
import check #A intchecker if the input data is ACTUALLY integer
import math


def pixelcompare(pic1,pic2,samplesize,dupesim):
    #print('pixelcompare here')

    index =0



    pic1=pic1.convert('RGBA')
    pic2=pic2.convert('RGBA')

    #pic2=Image.open(name2)

    width, height = pic2.size 
     #pixels
    same=0
    diff=0
    compared =0

    #pic2.convert('RGBA')
    #print(width)
    #print(height)
    #print(pic1)
    #print(pic2)
    #print(width)
    #print(height)




    if samplesize < 0 :
        pixels=32

    else:
        pixels=(width*height)*(samplesize/100)
        # v     ((math.sqrt(pixels))%2) != 0 or


    if pixels > (height*width):
        pixels= (height*width)
        print('yes')
        print(pixels)

    if  pixels ==0 :

        pixels+=1

    #debugging output
    #realpro=str(((pixels/(width*height))*100))
    #realpix=str(pixels)
    #print('testing: '+ realpro + ' % = ' + realpix+'pixels'  )


    hstep=int(height/(pixels/2))
    wstep=int(width/(pixels/2))

    if hstep == 0:
        hstep+=1
    if wstep == 0:
        wstep+=1
    #print(pic1.size)
    #print(pixels)
    #aprint(hstep )
    #print(wstep)
    for indexh in range(0,height,hstep):
        #print('hei')
        for indexw in range(0,width,wstep):
            randwidth= randint(indexw,indexw+wstep)
            randheight=randint(indexh,indexh+hstep)


            while randwidth >= width and randwidth !=0:
                randwidth=width -1
            while randheight >= height and randheight!=0:
                randheight=height -1

            #print(randwidth)
            #print(randheight)

            pixel1 = pic1.getpixel((randwidth,randheight))
            #print("==========")
            #print("testing"+str(randwidth)+" "+str(randheight))
            #print("values: " +str(r1) +" "+ str(g1) + " "+str(b1))


            pixel2 = pic2.getpixel((randwidth,randheight))

            #print("testing"+str(randwidth)+" "+str(randheight))
            #print("values: " +str(r2) +" "+ str(g2) + " "+str(b2))
            #print("=========")
            compared +=1
            if pixel1 == pixel2:

                same +=1


                #print('they are the same')
            else :
                diff +=1


                #print('they differentiate')
                if dupesim == 100:
                    #print('they are different')
                    #pic2.close()
                    return 0



    #print(str(same)+' / of ' +str(int(pixels)**2) + ' tested pixels, are the same ')
    #print(same)
    #print(pixels)

    compareresult= int(((same /compared ))*100)
    if compareresult>100:
        compareresult=100
    #pic2.close()
    #print(compareresult)
    return compareresult
