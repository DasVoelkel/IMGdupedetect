def intchecker(x):
    holder = 0
    y=0
    while y==0 :

        y=1
        try:
            holder=int(x)
        except ValueError:
            print('Wrong Data Type, int only!')
            y=0
            x = input()
        else:
            print('Your choice  is :' + x)
            return int(x)

def listchecker(list , x):
    index = 0
    form=str(x)
    y=0
    for index in range(0,len(list)) :
        print(index)
        if list[index] == form :
            y = 0
        elif list[index] != form :
            y = 1


    if y == 1 :
        list.append(form)   #list = list + x
    return list
