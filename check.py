import os, sys, inspect, glob
import dupecheck

from PIL import Image   #I am using Pillow! pip install pillow
import sizesort
#import check #A intchecker if the input data is ACTUALLY integer
import io
from os.path import basename

def intchecker(x):
    isint=True
    while isint :
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

    fixes=["*.jpg","*.png","*.jpeg","*.JPG","*.PNG","*.JPEG","*.tif","*.tiff","*.TIF","*.TIFF","*.dds","*.DDS"]
    count=0  #THIS IS A COUNTER NOT A BOOLEAN!
    for fix in fixes:
        for name in glob.glob(path+fix):
            count+=1

    return count

def checkformat(name1,name2):

    #print(name1)
    #print(name2)
    pic1 = name1
    pic2 = name2

    if (pic1.size != pic2.size) :
        return False
    elif (pic1.size == pic2.size):
        return True


def ETAcalc(path):
    fixes=["*.jpg","*.JPG","*.png","*.jpeg","*.JPEG","*.PNG","*.tif","*.tiff","*.TIF","*.TIFF","*.dds","*.DDS"]
    ETA=0
    jpgtime=1
    pngtime=1
    tiftime=1
    ddstime=1


    for fix in fixes:
        for name in glob.glob(path+fix):
            if fix == '*.jpg' or fix=='*.JPG' or fix=="*.jpeg" or fix == "*.JPEG":
                ETA=ETA+jpgtime
            if fix == '*.png' or fix=='*.PNG' :
                ETA=ETA+pngtime
            if fix == '*.tiff' or fix=='*.TIF' or fix=="*.tif" or fix == "*.TIFF":
                ETA=ETA+tiftime
            if fix == '*.dds' or fix=='*.DDS':
                ETA=ETA+ddstime
    return ETA


def getsizedictionary(path):
    print('creating sizedic')
    fixes=["*.jpg","*.JPG","*.png","*.jpeg","*.JPEG","*.PNG","*.tif","*.tiff","*.TIF","*.TIFF","*.dds","*.DDS"]
    sizedictionary={}
    for fix in fixes:
        for name in glob.glob(path+fix):
            print(name)
            pic=Image.open(name)
            sizedictionary[name]=pic.size
            pic.close()
    print('done')
    return sizedictionary





def getstatedictionary(path):
    print('creating statedic')
    statedictionary={}
    fixes=["*.jpg","*.JPG","*.png","*.jpeg","*.JPEG","*.PNG","*.tif","*.tiff","*.TIF","*.TIFF","*.dds","*.DDS"]
    for fix in fixes:
        for name in glob.glob(path+fix):
            statedictionary[name] = int(0)
    print('done')
    return statedictionary
