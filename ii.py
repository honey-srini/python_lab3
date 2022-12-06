#i
n=int(input("Enter the value of n:"))
i=1
j=1
while i<=n:
    j=1
    pattern=i
    while j<i*2:
        if j<i:
            print(pattern,end=" ")
            pattern-=1
        else:
            print(pattern,end=" ")
            pattern+=1
        j+=1
    i+=1
    print("")
