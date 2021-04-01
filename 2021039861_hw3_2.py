for i in range(1,10):
    if i<=5:
        print(" "*(5-i),"*"*(2*i-1)," "*(5-i),"\n",end='')
    else:
        print(" "*(i-5),"*"*((10-i)*2-1)," "*(i-5),"\n",end='')
