n=int(input("enter the size of an array"))
a=list(map(int,input("enter the numbers").split()))
if len(a)%2 != 0:
    print("alice is the winner")
elif n%2==0 and n%4==0:
    print("alice is the winner")
else:
    print("Bob is the winner")