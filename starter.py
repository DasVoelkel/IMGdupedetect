import dupemapper
import os

path = os.path.dirname(os.path.realpath(__file__))
main=dupemapper.mainfunction(path+"/pics",100)

for key in main:
	print (main[key] + ' ' + key)
