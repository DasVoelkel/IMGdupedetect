import os, sys, inspect
#import dupecheck

from PIL import Image   #I am using Pillow! pip install pillow
import sizesort
import check #A intchecker if the input data is ACTUALLY integer

# ============ Path set and error detection! =============
print('Where are the pics located? e.g. : /home/pictures ')
path = os.path.dirname(os.path.realpath(__file__))
print(path, end="")
path = path + input()
y=0
while y==0 :
    y=1
    try :
        os.chdir(path)
    except FileNotFoundError :
        print('This file Path does not exsist!')
        y=0

        path = os.path.dirname(os.path.realpath(__file__))
        print(path, end="")
        path = path + input()
#=============================================================END


print('Chose 1, for File sorting by size >> Size.txt ')
print('Chose 2, for dupechecking with %  of similarity')



holder = input()
userin = check.intchecker(holder)


if userin == 1:
    sizesort.sizemain()  #start Size differentiation
    print('')

if userin == 2:
    print('How similar should two pictures be to be considered the same ?(in % 0-100)')
    holder = input()
    dupesim = check.intchecker(holder)
    #dupecheck.dupemain(dupesim)    #check for dupes, in ALL the pictures
