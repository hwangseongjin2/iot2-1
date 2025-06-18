sum=0
i=1
while i<11:
    i=i+1
    if i%2==0:
        print("i=", i)
        sum=sum+i
    else:
        continue

print("sum=", sum)