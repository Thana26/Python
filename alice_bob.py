
n=int(input("enter the size of an array"))
a=list(map(int,input("enter the numbers").split()))
even_count=0
odd_count=0
for i in a:
    if i%2==0:even_count+=1
    else:odd_count+=1
# print(even_count,odd_count)

if even_count%2==0:
    #alice starts first picking odd numbersz
    b_chances=odd_count//2
    a_chances=odd_count-b_chances
    if a_chances%2==0:print('alice')
    else:print('bob')
    
else:
    #bob starts first picking odd numbers
    a_chances=odd_count//2
    b_chances=odd_count-a_chances
    if a_chances%2==0:print('alice')
    else:print('bob')