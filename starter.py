import dupemapper
import os


main=dupemapper.dupemapper("/home/dominik/Desktop/ImgDupe/IMGdupedetect/pics/")

for key in main:
    print (key + ' ' + main[key])
