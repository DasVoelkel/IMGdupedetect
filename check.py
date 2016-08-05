import os, sys, inspect, glob
import dupecheck

from PIL import Image   #I am using Pillow! pip install pillow
import sizesort
import check #A intchecker if the input data is ACTUALLY integer


def intchecker(x):
    holder = 0
    y=0
    while y==0 :

        y=1
        try:
            holder=int(x)
        except ValueError:
            print('Wrong Data Type, int only!')
            y=0
            x = input()
        else:
            print('Your choice  is :' + x)
            return int(x)

def listchecker(slist, x, y):
    #form=str(x)

    if len(slist) == 0:
        #print("definetly")
        z=True


    width = str(x)
    height= str(y)
    form = width + " " + height

    #print(width + " HERE " + height )

    #print(len(slist))
    z=True
    for index in slist :
        if index == form :
            z = False



    if z :
        #print("just added: " + form )
        slist.append(form)   #list = list + x




    return slist

def piccounter(path):

    fixes=["*.jpg","*.png","*.jpeg","*.JPEG","*.PNG","*.JPEG"]
    x=0
    for fix in fixes:
        for name in glob.glob(path+fix):
            x+=1

    return x

def checkformat(name1,name2): #pics sind doppelt offen !

    #print(name1)
    #print(name2)
    pic1 = name1
    pic2 = name2

    if (pic1.size != pic2.size) :

        return False
    elif (pic1.size == pic2.size):

        return True
    else :
        raise RuntimeError
