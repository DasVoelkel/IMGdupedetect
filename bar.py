import check




def setvalues(setprogress,setpicnr,path):
    global progress
    progress = setprogress
    global allpics
    global picnr
    global ETA

    ETA = check.ETAcalc(path)

    picnr=setpicnr
    allpics = picnr**2 #how many comparisons there are
    #print(' '*150,end='\r')

def incprog(): #one compare step at a time
    global progress
    progress +=1
    redraw()

def incstep(): #increment a whole step, a step is one compare to all pictures
    global progress
    global allpics
    progress = progress + picnr
    redraw()

def redraw():
    global allpics
    global progress
    global ETA
    if progress > allpics:
        progress=allpics
    bar=int((progress/allpics)*100)
    #print('x'*bar + "-"*(100-bar)+" progress: "+str(progress)+" of "+str(allpics) + "finished in (ETA:)" + str(ETA)+" s")
