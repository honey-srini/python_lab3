n=4
inner=0
outer=0
for i in range (1,n+1):
    for j in range(1,i+1):
        inner=inner+j
    outer=outer+inner
    inner=0
print(outer)
