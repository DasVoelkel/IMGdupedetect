import os, sys, inspect, glob #os to change directory, so the pictures can be in a subfolder or anywhere else
import dupecheck  #imports main function
from PIL import Image   #I am using Pillow! pip install pillow
import sizesort
import check #all kinds of functions wich check stuff, for form purposes in check.py
import bar #implements a loading bar, becasue just waiting is too boring
import time   # so you can measure and see the runtime of the whole programm
from os.path import basename # needed for shortening the filename out of path/filename
import shutil

def hasalpha(input,output):

    if not input.endswith("/"):
        input=input+'/'

    try :
        os.path.isdir(input)
    except FileNotFoundError :
        print("this file input does not exist!")
        return

    if not output.endswith("/"):
        output=output+'/'

    try :
        os.path.isdir(output)
    except FileNotFoundError :
        print("this file output does not exist!")
        return




    havealpha=[]
    noalpha=[]


    noalphaformats=[".jpg",".JPG",".jpeg","JPEG"]
    alphaformats=[".png",".PNG",".dds",".DDS",".tif",".tiff",".TIF",".TIFF"]

    #sizedictionary, sizelist = check.getsizedictionaryandsizelist(input)

    fixes=[".jpg",".png",".jpeg",".JPG",".PNG",".JPEG",".tif",".tiff",".TIF",".TIFF",".dds",".DDS"]

    count=0  #THIS IS A COUNTER NOT A BOOLEAN!
    for name in glob.glob(input+"*.*"):
        #print(name)
        filename, file_extension = os.path.splitext(name)
        #print(file_extension)
        if file_extension in fixes:
            count+=1


























    now=0

    for name in glob.glob(input+"*.*"):
        now +=1
        print(str(now)+" of " +str(count))
        #print("opening: "+name)
        o = time.time()
        image=Image.open(name)
        ##print("done")
        e=time.time()
        ##print(e-o)
        alpha=False

        if os.path.splitext(name)[-1] in noalphaformats:
            alpha = False
            noalpha.append(name)
            continue

        pic=image.convert('RGBA')

        width,height=pic.size
        # #print(height)
        # #print(width)
        start = time.time()
        for h in range(0,height-1):
            if alpha:
                break
            for w in range(0,width-1):
                if alpha:
                    break

                value = pic.getpixel((h,w))[-1]
                # #print(str(h) + " of h" + str(height))
                # #print(str(w) + " of w" + str(width))
                # #print(value)

                if value >= 255 :
                    alpha = False
                if value <= 254:
                    havealpha.append(name)
                    alpha=True
                    #print("appended to alpha")
        if not alpha:
            noalpha.append(name)
            #print("appended to noalpha")

        image.close()

        end = time.time()
        #print(end-start)


    alphadir=output+"AlphaPics"
    noalphadir=output+"NoAlphaPics"
    if not os.path.exists(alphadir):

        os.mkdir(alphadir)
    if not os.path.exists(noalphadir):
        os.mkdir(noalphadir)






    for name in havealpha:
        base=os.path.basename(name)
        filename,ending = os.path.splitext(base)

        ##print(os.path.splitext(base))
        shutil.copy(name,alphadir+"/"+filename+ending)

    for name in noalpha:
        base=os.path.basename(name)
        filename,ending = os.path.splitext(base)

        ##print(os.path.splitext(base))
        shutil.copy(name,noalphadir+"/"+filename+ending)


    return
