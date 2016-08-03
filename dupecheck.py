import os, sys, inspect, glob

from PIL import Image   #I am using Pillow! pip install pillow
import sizesort
import check
import pixelcheck



def dupemain(dupesim):
    dupesim = int(dupesim)

    picnr=check.piccounter()

    mainindex=0
    data = open("gensimilarity.txt", "w")
    similar = ['Testname1','Testname2']
    matchfound=[' ']
    simresult=0


    for name1 in glob.glob("*.jpg"):
        index =0
        pic1 = Image.open(name1)

        #match vorhanden dann nicht, wenn nicht dann checken
        z=0
        for index in range(0,len(matchfound)):
            if matchfound[index] == name1 :
                pic1.close()
                z=1




        if z==0 :
            z=0
            for name2 in glob.glob("*.jpg"):
                index=0
                pic2 = Image.open(name2)
                if name1 != name2 and check.checkformat(name1,name2) :
                    simresult = pixelcheck.pixelmain(name1,name2)

                    if simresult >=dupesim :
                        similar.append(name1)
                        similar.append(name2)  #noted for further inspection!

                        matchfound.append(str(name2))
                        for index in range(0,len(similar)):
                            data.write(similar[index])
                            data.write(";\n")
                            print(similar[index], end=";\n")



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
        else:
            z=0



    data.close()
