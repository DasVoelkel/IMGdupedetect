import os, sys, inspect, glob
import dupecheck

from PIL import Image   #I am using Pillow! pip install pillow
import sizesort
import check #A intchecker if the input data is ACTUALLY integer



def intchecker(x):
    isint=True
    while y :
        isint=False
        try:
            int(x)
        except ValueError:
            print('Wrong Data Type, int only!')
            isint=True
            x=input()
        else:
            print('Your choice  is :' + str(x))
            return int(x)

def listchecker(sizelist, x, y):
    #form=str(x)

    if len(sizelist) == 0:
        #print("definetly")
        z=True


    width = str(x)
    height= str(y)
    newsize = width + " " + height

    #print(width + " HERE " + height )

    #print(len(sizelist))
    z=True
    for index in sizelist :
        if index == newsize :
            z = False



    if z :
        #print("just added: " + newsize )
        sizelist.append(form)   #list = list + x




    return sizelist

def piccounter(path):

    fixes=["*.jpg","*.png","*.jpeg","*.JPEG","*.PNG","*.JPEG"]
    x=0  #THIS IS A COUNTER NOT A BOOLEAN!
    for fix in fixes:
        for name in glob.glob(path+fix):
            x+=1

    return x

def checkformat(name1,name2):

    #print(name1)
    #print(name2)
    pic1 = name1
    pic2 = name2

    if (pic1.size != pic2.size) :
        return False
    elif (pic1.size == pic2.size):
        return True
