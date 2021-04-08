print("Input first string : ",end='')
first = input()
print("Input second string : ",end='')
second = input()
first = list(first)
second = list(second)
answer= 0
count = len(first)

for i in range(1,count+1):
    if len(first) != len(second):
        print("Not circular identical!")
        break
    elif second == first:
        print("Circular string to right %d times." % answer)
        break
    else:
        copy=second[:]
        answer=answer+1
        for j in range(1,count):
            second[j]=copy[j-1]
        second[0] = copy[-1]
        
if answer >= count:
    print("Not circular identical!")
