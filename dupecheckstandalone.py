import os, sys, inspect
import dupecheck
import tkinter
from tkinter import *

from PIL import Image,ImageTk   #I am using Pillow! pip install pillow
import sizesort
import check #A intchecker if the input data is ACTUALLY integer
import bar
import time
#global path,similarity,samplesize,quit
global error#fnefnen
#AEGOSRGPAIEGNARÜGAWEGNWEGWO
class GUI(Frame):
    def __init__(self,parent=None):
        Frame.__init__(self,parent)
        Frame.pack(self)
        self.parent = parent
        #self=Tk()
        #self=Tk(parent)
        self.initialize()

        #Frame.pack(self)



    def initialize(self):
        #global error

        canvas = Canvas(self.parent, width=2000, height=1000)
        canvas.pack()
        canvas.create_line(0, 0, 200, 100)
        canvas.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))
        canvas.create_rectangle(50, 25, 150, 75, fill="blue")



        image = Image.open("logo.png")
        photo = ImageTk.PhotoImage(image)


        label1 = Label(self,image=photo)
        label1.image = photo # keep a reference!
        label1.grid(row = 5, column = 0, columnspan = 2, sticky=NW)
        Label(self, text="all directory paths have to be absolute! \n similarity weird values will be set to 100(such as negatives or >100) \n samplesize default = 16x16 pixels ( other neg vals = -1 )").grid(row = 5, column = 1, sticky=NW)

        self.parent.title("zkoor Picturecheck")

        self.error=False


        #self = Tk()
        #self.wm_itle("heyo")
        #label = Label(panel,text="ImgDupeDetect")
        #label.pack()
        Label(self, text="pic directory:").grid(row=0)
        Label(self, text="similarity:").grid(row=1)
        Label(self, text="SampleSize(-1=default 16x16):").grid(row=2)
        Label(self, text="output file:").grid(row=3)

        if self.error:
            Label(self,text="invalid entry",fg="red").grid(row=8)
        else:
            Label(self,text="          ").grid(row=8)


        path = os.path.dirname(os.path.realpath(__file__))

        self.e1 = Entry(self,width=50)
        self.e1.insert(0,path)
        self.e2 = Entry(self,width=50)
        self.e2.insert(0,str(100))
        self.e3 = Entry(self,width=50)
        self.e3.insert(0,str(-1))
        self.e4= Entry(self,width=50)
        self.e4.insert(0,path)

        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        self.e3.grid(row=2, column=1)
        self.e4.grid(row=3, column=1)

        button=Button(self, text='start dupecheck', command=self.startdupecheck).grid(row=8, column=1, sticky=W, pady=4)





    def startdupecheck(self):
        #global error

        #print("check init")
        #print(self.e1.get())
        self.path=str(self.e1.get())
        self.similarity=int(self.e2.get())
        self.samplesize=float(self.e3.get())
        self.output=str(self.e4.get())

        if not self.path.endswith("/"):
            self.path=self.path+'/'

        #print(self.path)
        self.error=False
        try:
            os.chdir(self.path)
        except:
            self.error=True




        # except FileNotFoundError :
        #     error=True
        #     print("YES")





        if not self.error:
            self.parent.destroy()

            if self.similarity > 100 or self.similarity<0:
                self.similarity=100
            if self.samplesize != -1 and self.samplesize < 0:
                self.samplesize=-1

            allpics = check.piccounter(self.path)
            bar.setvalues(0,allpics,self.path)
            start=time.time()
            dupecheck.checkfordupe(self.path,self.similarity,self.samplesize,self.output)
            end=time.time()
            print(end-start)

if __name__ == '__main__':
    root = Tk()

    app = GUI(root)
    root.mainloop()
