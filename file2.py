fo = open(“myfile.txt", "w")
fo.write('''This is 1st line
This is 2nd line
This is 3rd line
This is 4th line
This is 5th line''')
fo.close()
fo=open("foo.txt","r")
line = fo.readline()
print("Read Line: %s" % (line))
# Get the current position of the file.
pos = fo.tell()
print ("Current Position: %d" % (pos))
# Close opend file
fo.close()
