import os, glob

from PIL import Image   #I am using Pillow! pip install pillow
import sizesort
import check
import pixelcheck
from os.path import basename
import bar
import time



def checkfordupe(path,dupesim,samplesize):
    #print(path)
    samplesize=float(samplesize)
    dupesim = int(dupesim)
    dupemap={}
    sizedictionary=check.getsizedictionary(path)
    statedictionary=check.getstatedictionary(path)
    dupesfound=[]


    data = open("picture_similarity.txt", "w")


    #data.write('working with'+ str(dupesim))
    #data.write('similarity \n')
    #states
    # 0 -> not special
    # 1 -> was on pos1
    # 2 -> is a dupe

    #fixes=["*.jpg","*.png","*.jpeg","*.JPG","*.PNG","*.JPEG","*.tif","*.tiff","*.TIF","*.TIFF","*.dds","*.DDS"]

    for name1 in sizedictionary:
        if statedictionary[name1]==2 or statedictionary[name1]==1:
            continue

        statedictionary[name1]=1
        start=time.time()
        print('opening: '+name1)
        pic1=Image.open(name1)
        print('converting: '+name1)
        pic1.convert('RGBA')
        end=time.time()
        print('done took: ' + str(end-start))


        #bar.incstep()
        for name2 in sizedictionary:
            if name1 == name2 or sizedictionary[name1] != sizedictionary[name2] or statedictionary[name2]==1 or statedictionary[name2] == 2 :
                bar.incprog()
                continue
            start=time.time()

            print('comparing: ' + name1 + ' ' + str(sizedictionary[name1])+ ' with :' +name2 + ' ' + str(sizedictionary[name2]))
            simresult = pixelcheck.pixelcompare(pic1,name2,samplesize,dupesim)
            end=time.time()
            print('done took: '+ str(end-start))

            if simresult >= dupesim:
                statedictionary[name2]=2
                dupesfound.append(str(name2))
                #similar.append(name1)
                #similar.append(name2)
                dupemap[basename(name2)]=basename(name1)

            data.write(basename(name1))
            data.write(";")
            data.write(basename(name2))
            data.write(";")
            data.write(str(float(simresult)))
            data.write(";\n")
        pic1.close()


    data.close()
    print('\ntotal: '+str(check.piccounter(path))+ '  Dupes: ' + str(len(dupesfound))+ '  Unique: '+ str(  (check.piccounter(path))-(len(dupesfound))   ))
    return dupemap





def twocompare(dir1,dir2):
    try :
        pic1=Image.open(dir1)
    except FileNotFoundError:
        print('wrong file path on path1'+dir1)
        return None
        #NOT FileNotFoundError

    try:
        pic2=Image.open(dir2)
    except FileNotFoundError:
        print('wrong file path on path2'+dir2)
        return None


    simresult = pixelcheck.pixelcompare(pic1,pic2,-1,0)

    pic1.close()
    pic2.close()
    return simresult
