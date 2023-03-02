cl=cw=cc=0
f1=open("abcd.txt","r")
for i in f1:
    cl+=1
    words=line.split()
    cw+=len(words)
    cc+=len(line)
print("no.  of lines=",cl)
print("no.  of words=",cw)
print("no.  of character=",cc)
fi.close()
