from PIL import Image
import glob, os

size = 50,50

for infile in glob.glob("*logo.thumbnail.png"):
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)
    im.thumbnail(size)
    im.save(file + ".thumbnail", "png")
