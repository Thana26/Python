ch = input("enter the char value:")
if ch>='a'  and ch<='z' :
    print(ch,"is small alphabet:")
elif ch>='A' and ch<='Z' :
    print(ch,"is large alphabet:")
elif ch>='0' and ch<='9' :
    print(ch,"is number:")
else :
    print(ch,"is some special char ",ord(ch))
