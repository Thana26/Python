l=['sun','mon','tue','wed','thur','fri','sat']
n=int(input("enter number of days="))
day=input("enter 1st days=")
mydict={
    'sun':1,'mon':2,'tue':3,'wed':4,'thur':5,'fri':6,'sat':7
}
first=mydict.get(day)
for i in l:
    print(i,end=" ")
print(" ")

for i in range(1,first):
    print(" ",end="   ")
for i in range (1,first+1):
    print(i,end="   ")
print("")
for i in range (first+1,(first+1)+7):
    print(i,end="   ")
print("")
for i in range ((first+1)+7,(first+1)+14):
    print(i,end="  ")
print("")
for i in range ((first+1)+14,(first+1)+21):
    print(i,end="  ")
print("")
for i in range ((first+1)+21,n+1):
    print(i,end="  ")
print("")