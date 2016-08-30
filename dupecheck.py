import os, glob

from PIL import Image   #I am using Pillow! pip install pillow
import sizesort
import check
import pixelcheck
from os.path import basename
import bar
import time



def checkfordupe(path,dupesim,samplesize,output):
    # print(path)
    # print(dupesim)
    # print(samplesize)
    # print(output)  #




    samplesize=float(samplesize)
    dupesim = int(dupesim)
    dupemap={}
    sizedictionary,sizelist=check.getsizedictionaryandsizelist(path)
    statedictionary=check.getstatedictionary(path)
    dupesfound=[]
    enableoutput=isinstance(output, str)

    if enableoutput:
        dataname = os.path.join(output+"picture_similarity.txt")
        data = open(dataname, "w")
        logname = os.path.join(output+"pic_similarityLOG.txt")
        log = open(logname,"w")

    debug=False


    #data.write('working with'+ str(dupesim))
    #data.write('similarity \n')
    #states
    # 0 -> not special
    # 1 -> was on pos1
    # 2 -> is a dupe

    #fixes=["*.jpg","*.png","*.jpeg","*.JPG","*.PNG","*.JPEG","*.tif","*.tiff","*.TIF","*.TIFF","*.dds","*.DDS"]
    for sizes in sizelist:
        loaded=check.loadobjects(sizes,sizedictionary)
        for name1 in loaded:
            bar.incprog()
            if statedictionary[name1]==2 or statedictionary[name1]==1:
                continue
            statedictionary[name1]=1



            #bar.incstep()
            for name2 in loaded:
                #bar.incprog()
                if name1 == name2 or sizedictionary[name1] != sizedictionary[name2] or statedictionary[name2]==1 or statedictionary[name2] == 2 :
                    continue


                start=time.time()
                if debug : print('comparing: ' + name1 + ' ' + str(sizedictionary[name1])+ ' with :' +name2 + ' ' + str(sizedictionary[name2]))
                simresult = pixelcheck.pixelcompare(loaded[name1],loaded[name2],samplesize,dupesim)
                end=time.time()
                if debug : print('done took: '+ str(end-start))

                if simresult >= dupesim:
                    #bar.incstep()
                    statedictionary[name2]=2
                    dupesfound.append(str(name2))
                    #similar.append(name1)
                    #similar.append(name2)
                    dupemap[basename(name2)]=basename(name1)
                    if enableoutput:
                        data.write(basename(name1))
                        data.write(";")
                        data.write(basename(name2))
                        data.write(";")
                        data.write(str(float(simresult)))
                        data.write(";\n")

                if enableoutput:
                    log.write(basename(name1))
                    log.write(";")
                    log.write(basename(name2))
                    log.write(";")
                    log.write(str(float(simresult)))
                    log.write(";\n")
            #pic1.close()

        check.unloadobjects(loaded)
    if enableoutput:
        data.close()
        log.close()

    check.unloadobjects(loaded)

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
