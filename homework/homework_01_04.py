for y in range(1,6):
    for x in range(1,6):
        if(x-2>y or x+2<y or -x+4>y or -x+8<y):
            print("0",end="")
        else:
            print("1",end="")
    print("")