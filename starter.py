import dupemapper
import os


main=dupemapper.mainfunction("/home/dominik/Desktop/ImgDupe/IMGdupedetect/pics/",100)

for key in main:
	print (key + ' ' + main[key])
