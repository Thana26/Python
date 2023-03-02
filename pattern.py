string=input("enter the string:")
l=len(string)
for i in range(l):
	for j in range(i+1):
		print(string[j],end=" ")
	print()
