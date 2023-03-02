d={}
n=int(input("Enter the number of key-value pairs of the dictionary:"))
for i in range(n):
    k,v=map(int,input("enter the key and value for index{} separated by ',' :".format(i)).split(','))
    d.update({k:v})
print(d)
c=int(input("enter the value to find in the dictionary:"))
k1=[k for k,v in d.items() if v==c]
print("Following are the keys found for the value {}".format(c))
print(*k1,sep='\n')
