import os, glob
from PIL import Image   #I am using Pillow! pip install pillow
import sizesort
import check
import pixelcheck
from os.path import basename
import bar
import time
import shutil, errno


def hasalpha(input,output):
    havealpha=[]
    noalpha=[]


    noalphaformats=[".jpg",".JPG",".jpeg","JPEG"]
    alphaformats=[".png",".PNG",".dds",".DDS",".tif",".tiff",".TIF",".TIFF"]

    #sizedictionary, sizelist = check.getsizedictionaryandsizelist(input)

    for name in glob.glob(input+"*.*"):
        print("opening: "+name)
        o = time.time()
        image=Image.open(name)
        print("done")
        e=time.time()
        print(e-o)
        alpha=False

        if os.path.splitext(name)[-1] in noalphaformats:
            alpha = False
            noalpha.append(name)
            continue

        pic=image.convert('RGBA')

        width,height=pic.size
        # print(height)
        # print(width)
        start = time.time()
        for h in range(0,height-1):
            if alpha:
                break
            for w in range(0,width-1):
                if alpha:
                    break

                value = pic.getpixel((h,w))[-1]
                # print(str(h) + " of h" + str(height))
                # print(str(w) + " of w" + str(width))
                # print(value)

                if value >= 255 :
                    alpha = False
                if value <= 254:
                    havealpha.append(name)
                    alpha=True
                    print("appended to alpha")
        if not alpha:
            noalpha.append(name)
            print("appended to noalpha")

        image.close()

        end = time.time()
        print(end-start)


    alphadir=output+"AlphaPics"
    noalphadir=output+"NoAlphaPics"
    if not os.path.exists(alphadir):

        os.mkdir(alphadir)
    if not os.path.exists(noalphadir):
        os.mkdir(noalphadir)






    for name in havealpha:
        base=os.path.basename(name)
        filename,ending = os.path.splitext(base)

        print(os.path.splitext(base))
        shutil.copy(name,alphadir+"/"+filename+ending)

    for name in noalpha:
        base=os.path.basename(name)
        filename,ending = os.path.splitext(base)

        print(os.path.splitext(base))
        shutil.copy(name,noalphadir+"/"+filename+ending)


    return
