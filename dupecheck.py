import os, glob

from PIL import Image   #I am using Pillow! pip install pillow
import sizesort
import check
import pixelcheck
from os.path import basename
import bar



def dupemain(path,dupesim,samplesize):
    #print(path)
    samplesize=float(samplesize)
    dupesim = int(dupesim)
    dupemap={}


    data = open("picture_similarity.txt", "w")

    #data.write('working with'+ str(dupesim))
    #data.write('similarity \n')
    similar = [] #similarpictures
    wasonpos1=[]
    dupesfound=[]

    fixes=["*.jpg","*.png","*.jpeg","*.JPEG","*.PNG","*.JPEG"]


    for fixmain in fixes:
        #print('fixmain: '+fixmain)
        for name1 in glob.glob(path+fixmain):
            #print ("comping:"+ name1)
            pic1 = Image.open(name1)
            #match vorhanden dann nicht, wenn nicht dann checken
            newpos1=True
            for index in dupesfound:
                if index == name1 :
                    #print('DUPE')
                    pic1.close()
                    newpos1=False

            if newpos1 :
                #jeder fix mit jedem fix
                for fixmini in fixes:
                    #print('fixmini: '+fixmini)
                    for name2 in glob.glob(path+fixmini):
                        #print("mit: "+ name2)
                        pic2 = Image.open(name2)
                        newpos2=True
                        bar.incprog() # ----
                        for index in wasonpos1:
                            if index == name2:
                                #print('taken')
                                pic2.close()
                                newpos2=False



                        if newpos2:
                            newpos2=True
                            if name1 != name2 and check.checkformat(pic1,pic2) :

                                simresult = pixelcheck.pixelmain(pic1,pic2,samplesize,dupesim)

                                if simresult >=dupesim :
                                    similar.append(name1)
                                    similar.append(name2)  #noted for further inspection!

                                    bar.incstep() #---

                                    dupesfound.append(str(name2))

                                    dupemap[basename(name2)]=basename(name1) #create and expand dictionary

                                    data.write(basename(name1))
                                    data.write(";")
                                    data.write(basename(name2))
                                    data.write(";")
                                    data.write(str(float(simresult)))
                                    data.write(";\n")




                                #WRITE RESULTS IN A FILE [NAME and NAME , SIMILARITY = simresult ]
                                wasonpos1.append(str(name1))


                            pic2.close()
                        else:
                            newpos2=True
            else:
                newpos1=True


            pic1.close()
    data.close()

    print('\ntotal: '+str(check.piccounter(path))+ '  Dupes: ' + str(len(dupesfound))+ '  Unique: '+ str(  (check.piccounter(path))-(len(matchfound2))   ))


    #return DICTIONARY MAP!


    return dupemap


def twocomp(dir1,dir2):
    try :
        pic1=Image.open(dir1)
    except FileNotFoundError:
        print('wrong file path on path1'+path1)
        return None
        #NOT FileNotFoundError

    try:
        pic2=Image.open(dir2)
    except FileNotFoundError:
        print('wrong file path on path2'+path2)
        return None


    simresult = pixelcheck.pixelmain(pic1,pic2,-1,0)

    pic1.close()
    pic2.close()
    return simresult
