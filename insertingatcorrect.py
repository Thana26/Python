a=[1,2,3,4,6]
a.sort()
b=a[-1]
sum=0
for i in a:
    sum=sum+i

total=b*(b+1)
total1=total//2
missing=total1-sum
print(missing)
a.insert(missing-1,missing)
print(a)