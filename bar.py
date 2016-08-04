import check




def setvalues(setprogress,setpicnr):
    global progress
    progress = setprogress
    global comp
    global picnr
    picnr=setpicnr
    comp = picnr**2 #how many comparisons there are
    #print(' '*150,end='\r')

def incprog():
    global progress
    progress +=1
    redraw()

def incstep():
    global progress
    global comp
    progress = progress + picnr
    redraw()

def redraw():
    global comp
    global progress
    if progress > comp:
        progress=comp
    bar=int((progress/comp)*100)
    print('x'*bar + "-"*(100-bar)+" progress: "+str(progress)+" of "+str(comp),end='\r')
