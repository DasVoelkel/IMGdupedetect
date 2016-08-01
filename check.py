def checker(x):
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
            return x
