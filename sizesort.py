from PIL import Image
import glob, os
import check

def sizemain() :
    #im = Image.open("original.jpg")
    #print(im.format, im.size, im.mode)
    data = open("IMGDATA.txt", "w")

    sizelist = ['100x100','200x200']
    #print ( str(len(sizelist)))
    index = 0
    for name in glob.glob("*.jpg"):
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

    for name in glob.glob("*.png"):
        pic = Image.open(name)
        data.write(name)               #print NAME FORMAT SIZE
        data.write(";" + str(pic.format))
        width,height = pic.size
        width = str(width)
        height = str(height)

        data.write(";" + width)
        data.write(" " + height)
        data.write("\n")

        #checking exsisting sizes and adding missing onse
        sizelist = check.listchecker(sizelist,width,height)
        #================================================
        pic.close()

    for name in glob.glob("*.jpeg"):
        pic = Image.open(name)
        data.write(name)               #print NAME FORMAT SIZE
        data.write(";" + str(pic.format))
        width,height = pic.size

        width = str(width)
        height = str(height)

        data.write(";" + width)
        data.write(" " + height)
        data.write("\n")

        #checking exsisting sizes and adding missing onse
        sizelist = check.listchecker(sizelist,width,height)
        #================================================
        pic.close()

    #write sizes!
    print(len(sizelist))
    for index in range(0,(len(sizelist))) :
        data.write(sizelist[index])
        data.write(";")
        print(sizelist[index], end=";")

    data.close()
