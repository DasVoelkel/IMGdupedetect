#import dupecheck
#import szesort
import check #A checker if the input data is ACTUALLY integer
import os

print('Where are the pics located? (errors might be devastating)')


print('Chose 1, for File sorting by size >> Size.txt ')
print('Chose 2, for dupechecking with %  of similarity')



holder = input()
userin = check.checker(holder)


if(userin == '1') :

    #sizesort.sizemain()  #start Size differentiation


if(userin == '2')  :
    print('How similar should two pictures be to be considered the same ?(in % 0-100)')
    holder = inout()
    dupesim = check.checker(holder)

    #dupecheck.dupemain(dupesim)    #check for dupes, in ALL the pictures
