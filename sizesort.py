from PIL import Image
import glob, os
import check
import bar

def sizemain():
    #im = Image.open("original.jpg")
    #print(im.format, im.size, im.mode)
    data = open("IMGDATA.txt", "w")

    sizelist = []
    #print ( str(len(sizelist)))

    fixes=["*.jpg","*.png","*.jpeg","*.JPEG","*.PNG","*.JPEG"]



    for fix in fixes:
        for name in glob.glob(fix):

            #bar.incstep()

            pic = Image.open(name)
            data.write(name)               #print NAME FORMAT SIZE
            data.write(";" + str(pic.format))
            width,height = pic.size

            width = str(width)
            height = str(height)

            data.write(";" + width)
            data.write(" " + height)
            data.write("\n")

            #print(pic.size)
            #checking exsisting sizes and adding missing onse
            sizelist = check.listchecker(sizelist,width,height)
            #================================================
            pic.close()


    #write sizes!

    for index in sizelist :
        data.write(index)
        data.write(";")
        #print(index, end=";")

    data.close()
