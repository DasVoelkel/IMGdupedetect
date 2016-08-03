

def barmain():
    progress,comp = main.getblobal()
    for i in range(0,comp):
        print('x'*(progess//comp),end='\r')
