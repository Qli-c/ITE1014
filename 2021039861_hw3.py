n = 0
fi = [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
while n!=4:
    print("*************\n1.Calculate\n2.Show it!\n3.Initialize\n4.Quit\n*************\nInput : ", end='')
    n = int(input())    
    if n==1:
        print("Input the number : ",end='')
        end = int(input())
        if end>20:
            break
        
        for i in range(2,end+1):
            fi[i]=fi[i-1]+fi[i-2]
            
    if n==2:
        for a in range(0,end+1):
            print("%i "%fi[a],end='')
        print('')
        
    if n==3:
        fi = [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        end = 1
        
    if n==4:
        break
    
