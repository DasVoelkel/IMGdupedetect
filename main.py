import os, sys, inspect
import dupecheck

from PIL import Image   #I am using Pillow! pip install pillow
import sizesort
import check #A intchecker if the input data is ACTUALLY integer
import bar

#progress bar




# ============ Path set and error detection! =============
print('Where are the pics located? e.g. : /home/pictures ')
path = os.path.dirname(os.path.realpath(__file__))
print(path +"/pics", end="")
path = path + "/pics" + input()
print(path)

y=True
while y :
    y=False
    try :
        os.chdir(path)
    except FileNotFoundError :
        print('This file Path does not exsist!')
        y=True

        path = os.path.dirname(os.path.realpath(__file__))
        print(path +"/pics", end="")
        path = path + "/pics" +input()
#=============================================================END


print('Chose 1, for File sorting by size >> IMGdata.txt ')
print('Chose 2, for dupechecking with %  of similarity >>gensimilarity')



userin = input()
userin = check.intchecker(userin)


if userin == 1:
    comp = check.piccounter()
    sizesort.sizemain()  #start Size differentiation


if userin == 2:
    print('How similar should two pictures be to be considered the same ?(in % 0-100)')
    similarity = input()
    similarity = check.intchecker(similarity)
    print('What is oyur sample size? (how many pixels should be compared ?)')
    samplesize = input()
    samplesize = check.intchecker(samplesize)

    dupecheck.dupemain(similarity,samplesize)    #check for dupes, in ALL the pictures
