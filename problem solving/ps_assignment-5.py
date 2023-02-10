from sqlalchemy import true

n=int(input("enter the size of an array"))
a=list(map(int,input("enter the numbers").split()))
mov=n//2                                              #find number moves for alice if n is even                                  
q=mov
even,odd=0,0
for i in a:
    if i%2==0:even+=1
    else:odd+=1
while true:
    if q<0:
        print('bob')                                   #if their is no moves for alice bob wins
        break                                           #Alice and bob will try to choose all the even elements from array and then choose odd part.
    alice_even=q+q-1                                            #odd number of even numbers for alice
    alice_odd=mov-q+mov-q                                       #odd number of odd numbers for alice
    if (even>=alice_even and odd>=alice_odd):
        print('alice')
        break
    alice_even=q+q                                              #Simillarly here we take odd part first after compliting we go for even part.
    alice_odd=mov-q+mov-q-1
    if (even>=alice_even and odd>=alice_odd):
        print('alice')
        break
    q-=2                                                