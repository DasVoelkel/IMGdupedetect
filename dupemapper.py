import os, sys, inspect
import dupecheck

from PIL import Image   #I am using Pillow! pip install pillow
import sizesort
import check #A intchecker if the input data is ACTUALLY integer
import bar
import time





#progress bar







def mainfunction(dir,simularity=100):
    start = time.time()
    os.chdir(dir)

    comp = check.piccounter()
    bar.setvalues(0,comp)

    end = time.time()
    print(end - start)

    dupemap=dupecheck.dupemain(simularity,-1)
    return dupemap
