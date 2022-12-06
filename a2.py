x=2
n=5
sum=0
for i in range(1,n+1):
    if(i%2==0):
        i=x**i
        sum=sum+i
    else:
        i=x**i
        sum=sum-i
print(sum)
