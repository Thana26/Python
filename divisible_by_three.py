x=int(input("enter x:"))
if x%2 ==0:
    if x%3==0:
        print(x," is divisible by 2 and 3")
    else:
        print(x," is divisible by 2 and not by 3")
elif x%3==0:
    print(x," is divisible by 3 and not by 2")
else:
    print (x, "is not divisible by both")
