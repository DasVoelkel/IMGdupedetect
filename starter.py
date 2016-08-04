import dupemapper
import os


main=dupemapper.mainfunction("/pics/",100)

for key in main:
	print (key + ' ' + main[key])
