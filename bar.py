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

    bar=int((progress/comp)*100)
    print('x'*bar + "-"*(100-bar),end='\r')
