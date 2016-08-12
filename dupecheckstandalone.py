import os, sys, inspect
import dupecheck
import tkinter
from tkinter import *

from PIL import Image   #I am using Pillow! pip install pillow
import sizesort
import check #A intchecker if the input data is ACTUALLY integer
import bar
import time
#global path,similarity,samplesize,quit
global error

class GUI():
    def __init__(self,parent):
        self.parent = parent
        self.panel=Tk()
        #self.panel=Tk(parent)
        self.initialize()



    def initialize(self):
        #global error


        #self.panel = Tk()
        #self.panel.Title("heyo")
        #label = Label(panel,text="ImgDupeDetect")
        #label.pack()
        Label(self.panel, text="pic directory").grid(row=0)
        Label(self.panel, text="similarity:").grid(row=1)
        Label(self.panel, text="SampleSize:").grid(row=2)
        Label(self.panel, text="output file:").grid(row=3)




        path = os.path.dirname(os.path.realpath(__file__))

        self.e1 = Entry(self.panel,width=50)
        self.e1.insert(0,path)
        self.e2 = Entry(self.panel,width=50)
        self.e2.insert(0,str(100))
        self.e3 = Entry(self.panel,width=50)
        self.e3.insert(0,str(-1))
        self.e4= Entry(self.panel,width=50)
        self.e4.insert(0,path)

        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        self.e3.grid(row=2, column=1)
        self.e4.grid(row=3, column=1)

        button=Button(self.panel, text='start dupecheck', command=self.startdupecheck).grid(row=8, column=1, sticky=W, pady=4)

        #self.panel.mainloop



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
        error=False
        try:
            os.chdir(self.path)
        except:
            error=True




        # except FileNotFoundError :
        #     error=True
        #     print("YES")
        if error:
            Label(self.panel,text="invalid entry",fg="red").grid(row=8)
        else:
            Label(self.panel,text="          ").grid(row=8)




        if not error:
            self.panel.destroy()

            allpics = check.piccounter(self.path)
            bar.setvalues(0,allpics,self.path)
            start=time.time()
            dupecheck.checkfordupe(self.path,self.similarity,self.samplesize,self.output)
            end=time.time()
            print(end-start)





app = GUI(None)
mainloop()
