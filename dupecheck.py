import os, sys, inspect, glob

from PIL import Image   #I am using Pillow! pip install pillow
import sizesort
import check
import pixelcheck
import bar



def dupemain(dupesim,samplesize):
    dupesim = int(dupesim)



    data = open("gensimilarity.txt", "w")

    data.write('working with'+ str(dupesim))
    data.write('similarity \n')
    similar = [] #similarpictures
    matchfound=[]
    simresult=0

    fixes=["*.jpg","*.png","*.jpeg"]

    for fixmain in fixes:

        for name1 in glob.glob(fixmain):

            pic1 = Image.open(name1)

            #match vorhanden dann nicht, wenn nicht dann checken
            z=True
            for index in matchfound:
                if index == name1 :
                    pic1.close()
                    z=False
            if z :
                z=True
                #jeder fix mit jedem fix
                for fixmini in fixes:

                    for name2 in glob.glob(fixmini):
                        pic2 = Image.open(name2)
                        bar.incprog() # ----
                        if name1 != name2 and check.checkformat(pic1,pic2) :
                            simresult = pixelcheck.pixelmain(pic1,pic2,samplesize,dupesim)

                            if simresult >=dupesim :
                                similar.append(name1)
                                similar.append(name2)  #noted for further inspection!

                                bar.incstep() #---
                                matchfound.append(str(name2))



                            #WRITE RESULTS IN A FILE [NAME and NAME , SIMILARITY = simresult ]

                            data.write(name1)
                            data.write(";")
                            data.write(name2)
                            data.write(";")
                            data.write(str(float(simresult)))
                            data.write(";\n")
                        pic2.close()
            else:
                z=True


            pic1.close()
    data.close()
