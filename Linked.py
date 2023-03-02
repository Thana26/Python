class student:
    def __init__(self,roll):
        self.data=roll
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def insertatbegin(self,roll):
        new=student(roll)
        if(self.head==None):
            self.head=new
        else:
            new.next=self.head
            self.head=new
    def insertbefore(self,roll,pos):
        new=student(roll)
        temp=self.head
        temp1=None
        if(self.head==None):
            print("No values")
        else:
            i=1
            while(temp!=None):
                if i==pos:
                    break
                i=i+1
                temp1=temp
                temp=temp.next
                new.next=temp
                temp1.next=new


    def display(self):
        temp=self.head
        if(temp==None):
            print("No elements are present")
        else:
            while(temp!=None):
                print(temp.data,end=" ")
                temp=temp.next
s=sll()
k=[int(a) for a in input("enter num:").split()]
for i in k:
    s.insertatbegin(i)
s.display()
print(" ")
a=int(input())
b=int(input())
s.insertbefore(a,b)
s.display()


