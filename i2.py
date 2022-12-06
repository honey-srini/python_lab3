#i ii diagonal $
n = int(input("Enter the value of n: "))
i=1
while i<=n:
    j=1
    while j<=n:
        if(i==j):
            print("$",end=" ")
        elif(i==1 or j==1 or i==n or j==n):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        j+=1
    print(" ")
    i+=1
