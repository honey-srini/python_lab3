arr=[]
for l in range (1,6):
    arr.append(int(input("Enter the {0} number :" .format(l))))
for i in range(0,5):
    for j in range(0,i):
        print(" ",end=" ")
    for k in range(i,5):
        print(arr[k],end=" ")
    print(" ")
    
for i in range(0,5):
    for k in range(0,i+1):
        print(arr[k],end=" ")
    print(" ")
        
                   
