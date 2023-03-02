st = input("enter string")
s1 = ''
for i in st:
    s1 = s1 + chr(ord(i) + 1)
print(s1)
