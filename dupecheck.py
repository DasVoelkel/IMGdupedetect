import os, sys, inspect, glob

from PIL import Image   #I am using Pillow! pip install pillow
import sizesort
import check
import pixelcheck
import bar



def dupemain(path,dupesim,samplesize):
    dupesim = int(dupesim)
    dupemap={}


    data = open("gensimilarity.txt", "w")

    #data.write('working with'+ str(dupesim))
    #data.write('similarity \n')
    similar = [] #similarpictures
    matchfound1=[]
    matchfound2=[]
    simresult=0

    fixes=["*.jpg","*.png","*.jpeg","*.JPEG","*.PNG","*.JPEG"]


    for fixmain in fixes:
        #print('fixmain: '+fixmain)
        for name1 in glob.glob(path+fixmain):
            #print ("comping:"+ name1)
            pic1 = Image.open(name1)
            #match vorhanden dann nicht, wenn nicht dann checken
            z=True
            for index in matchfound2:
                if index == name1 :
                    #print('DUPE')
                    pic1.close()
                    z=False

            if z :
                z=True
                #jeder fix mit jedem fix
                for fixmini in fixes:
                    #print('fixmini: '+fixmini)
                    for name2 in glob.glob(path+fixmini):
                        #print("mit: "+ name2)
                        pic2 = Image.open(name2)
                        p=True
                        bar.incprog() # ----
                        for index in matchfound1:
                            if index == name2:
                                #print('taken')
                                pic2.close()
                                p=False



                        if p:
                            p=True
                            if name1 != name2 and check.checkformat(pic1,pic2) :

                                simresult = pixelcheck.pixelmain(pic1,pic2,samplesize,dupesim)

                                if simresult >=dupesim :
                                    similar.append(name1)
                                    similar.append(name2)  #noted for further inspection!

                                    bar.incstep() #---

                                    matchfound2.append(str(name2))

                                    dupemap[name2]=name1

                                    data.write(name1)
                                    data.write(";")
                                    data.write(name2)
                                    data.write(";")
                                    data.write(str(float(simresult)))
                                    data.write(";\n")




                                #WRITE RESULTS IN A FILE [NAME and NAME , SIMILARITY = simresult ]
                                matchfound1.append(str(name1))


                            pic2.close()
                        else:
                            p=True
            else:
                z=True


            pic1.close()
    data.close()

    print('\ntotal: '+str(check.piccounter())+ '  Dupes: ' + str(len(matchfound2))+ '  Unique: '+ str(  (check.piccounter())-(len(matchfound2))   ))


    #return DICTIONARY MAP!


    return dupemap
