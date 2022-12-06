#i iv
n= int(input("Enter the number of rows: "))  
i=1
while i<n*2:
    if i<=n:
        print("*"*i)
    else:
        print("*"*((n*2)-i))
    i+=1
