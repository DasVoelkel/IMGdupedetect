"IMGdupedetect"
Stnad 15:49 4.Aug.2016

I USE: Pillow3.3
Python3 , on Linux

Main function :
compare a bunch of pictures with one another, see for duplicates over a given threshhold
The results are written down and output into a txt file.

Function:
Position 1 is " original " Position
position 2 is the "dupe " Position - Pos1 gets compared with Pos2

The code compares a given % of the whole pictures size with one another.
(only pics of the same size will get compared.)
the % result is written down.


Optimization:
If Pos2 is a match with Pos1 it will not go into pos1 and will be skipped,
with this you safe one comparison with EACH picture.

If Pos1 has been compared with pos2
when pos2 is in pos1 it won't compare to the picture wich was in pos 1 before.
since it has already compared to that picture

features:
there is a loading bar !
also you can just output a ton of picture data without comparing the pictures
