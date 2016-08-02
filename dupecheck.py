import os, sys, inspect, glob

from PIL import Image   #I am using Pillow! pip install pillow
import sizesort
import check
import pixelcheck



def dupemain(dupesim):
    dupesim = int(dupesim)

    picnr=check.piccounter()
    index=0
    mainindex=0
    data = open("gensimilarity.txt", "w")
    similar = ['Testname1','Testname2']
    simresult=0


    for name1 in glob.glob("*.jpg"):
        pic1 = Image.open(name1)

        for name2 in glob.glob("*.jpg"):
            pic2 = Image.open(name2)
            if name1 != name2 and check.checkformat(name1,name2) :
                simresult = pixelcheck.pixelmain(name1,name2)

                if simresult >=dupesim :
                    similar.append(name1)
                    similar.append(name2)  #noted for further inspection!




                #WRITE RESULTS IN A FILE [NAME and NAME , SIMILARITY = simresult ]
                data.write(name1)
                data.write(" with ")
                data.write(name2)
                data.write(" had ")
                data.write(str(simresult))
                data.write("%")
                data.write(";\n")
                pic2.close()
        pic1.close()
    data.close()
