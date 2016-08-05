import os #os to change directory, so the pictures can be in a subfolder or anywhere else
import dupecheck  #imports main function
from PIL import Image   #I am using Pillow! pip install pillow
import sizesort
import check #all kinds of functions wich check stuff, for form purposes in check.py
import bar #implements a loading bar, becasue just waiting is too boring
import time   # so you can measure and see the runtime of the whole programm
from os.path import basename # needed for shortening the filename out of path/filename

def dupemapper(dir,simularity=100):
    #path = os.path.dirname(os.path.realpath(__file__))
    path = dir
    start = time.time()

    if not path.endswith("/"):
        path=path+'/'

    try :
        os.path.isdir(path)
    except FileNotFoundError :
        print("this file path does not exist!")
        main={}
        return main


    allpics = check.piccounter(path)
    bar.setvalues(0,allpics)




    dupemap=dupecheck.checkfordupe(path,simularity,-1)
    end = time.time()
    print('it took :' + str(end - start))
    return dupemap

def exactcompare(dir1,dir2):
    start = time.time()

    dupenumber = dupecheck.twocompare(dir1,dir2)

    end = time.time()
    print('it took :' + str(end - start))
    return dupenumber
