str = "YOLO LIFE"
# create dictionary to store key value pair
dict = {}

for i in str:
    # if i already appears as key in dict, increment the count
    if i in dict:
        dict[i] += 1

    # else i appears for the first time, add to dict
    else:
        dict[i] = 1

# printing result 
print(dict)

d=dict.values()
print(len(d))
odd,even=0,0
for t in d:
    if t%2==0:
        even=even+1
    else:
        odd=odd+1

leng=len(str)

if(leng%2==0 and odd%2==0):
    print('palindrome')

