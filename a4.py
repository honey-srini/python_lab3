import math
x=2
n=5
sum=0
 
for i in range(0,n):
    if(i%2==0):
        i=(x**i)/(math.factorial(i))
        sum+=i
    else:
        i=(x**i)/(math.factorial(i))
        sum-=i
print(sum)

