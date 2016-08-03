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

def listchecker(list, x, y):
    index = 0
    #form=str(x)
    z=0
    width = str(x)
    height= str(y)
    form = width + " " + height
    #print(width + "HERE" + height )

    for index in range(0,len(list)) :
        if list[index] == form :
            z = 0
        elif list[index] != form :
            z = 1


    if z == 1 :
        list.append(form)   #list = list + x
    return list

def piccounter():
    x=0
    for name in glob.glob("*.jpg"):
        x+=1
    for name in glob.glob("*.png"):
        x+=1
    for name in glob.glob("*.jpeg"):
        x+=1
    return x

def checkformat(name1,name2):
    #print(name1)
    #print(name2)
    pic1 = Image.open(name1)
    pic2 = Image.open(name2)

    if (pic1.size != pic2.size) :
        pic1.close()
        pic2.close()
        return False
    elif (pic1.size == pic2.size):
        pic2.close()
        pic1.close()
        return True
    else :
        raise RuntimeError
