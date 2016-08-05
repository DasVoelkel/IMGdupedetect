import os, sys, inspect
import dupecheck

from PIL import Image   #I am using Pillow! pip install pillow
import sizesort
import check #A intchecker if the input data is ACTUALLY integer
import bar
import time

start = time.time()








# ============ Path set and error detection! =============
print('Where are the pics located? e.g. : /home/pictures ')
path = os.path.dirname(os.path.realpath(__file__))
print(path +"/pics/", end="")
path = path + "/pics/" + input()
print(path)

y=True
while y :
    y=False
    try :
        os.path.isdir(path)
    except FileNotFoundError :
        print('This file Path does not exsist!')
        y=True

        path = os.path.dirname(os.path.realpath(__file__))
        print(path +"/pics/", end="")
        path = path + "/pics/" +input()
        print(path)
#=============================================================END
if not path.endswith("/"):
    path=path+'/'







print('Chose 1, for File sorting by size >> IMGdata.txt ')
print('Chose 2, for dupechecking with %  of similarity >>picture_similarity.txt')



userin = input()
userin = check.intchecker(userin)



if userin == 1:
    #allpics = check.piccounter(path)
    #bar.setvalues(0,allpics)   #function too quick for a loading bar, it bugs out
    sizesort.sizemain()  #start Size differentiation

    end = time.time()
    print(end - start)


if userin == 2:
    print('How similar should two pictures be to be considered the same ?(in % 0-100)')
    similarity = input()
    similarity = check.intchecker(similarity)
    print('how much ( in %) of the picture should be checked(enter -1 for default=32Pixels per picture) ')
    samplesize = str(input())
    if samplesize == '':
        samplesize = float(-1)

    allpics = check.piccounter(path)
    bar.setvalues(0,allpics) #VORLÄUFIG

    dupecheck.dupemain(path,similarity,float(samplesize))    #check for dupes, in ALL the pictures


    end = time.time()
    print(end - start)
