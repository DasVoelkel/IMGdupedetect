import os, sys, inspect, glob

from PIL import Image   #I am using Pillow! pip install pillow
import sizesort
import check
import pixelcheck



def dupemain(dupesim,samplesize):
    dupesim = int(dupesim)



    data = open("gensimilarity.txt", "w")
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
                        if name1 != name2 and check.checkformat(pic1,pic2) :
                            simresult = pixelcheck.pixelmain(pic1,pic2,samplesize)

                            if simresult >=dupesim :
                                similar.append(name1)
                                similar.append(name2)  #noted for further inspection!

                                matchfound.append(str(name2))



                            #WRITE RESULTS IN A FILE [NAME and NAME , SIMILARITY = simresult ]
                            data.write(name1)
                            data.write(" with ")
                            data.write(name2)
                            data.write(" had ")
                            data.write(str(simresult))
                            data.write("%")
                            data.write(";\n")
                        pic2.close()
            else:
                z=True


            pic1.close()
    data.close()
