a=input("enter the email adress:")
print(a)
count=0
for i in a:
    if(i=='@'):
        break
    count=count+1
b=(a[0:count],a[count+1:])
print(b)
