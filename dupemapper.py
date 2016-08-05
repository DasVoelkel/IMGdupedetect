import os #os to change directory, so the pictures can be in a subfolder or anywhere else
import dupecheck  #imports main function
from PIL import Image   #I am using Pillow! pip install pillow
import sizesort
import check #all kinds of functions wich check stuff, for form purposes in check.py
import bar #implements a loading bar, becasue just waiting is too boring
import time   # so you can measure and see the runtime of the whole programm
from os.path import basename # needed for shortening the filename out of path/filename

def mainfunction(dir,simularity=100):
    #path = os.path.dirname(os.path.realpath(__file__))
    path = dir
    start = time.time()
    os.chdir(path)

    comp = check.piccounter()
    bar.setvalues(0,comp)




    dupemap=dupecheck.dupemain(path,simularity,-1)
    end = time.time()
    print('it took :' + str(end - start))
    return dupemap
