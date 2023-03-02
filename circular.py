class student:
    def __init__(self,roll):
        self.data=roll
        self.next=None
class cll:
    def __init__(self):
        self.head=None
        self.tail=None
    def insertatbegin(self,roll):
        new=student(roll)
        if(self.head==self.tail==None):
            self.head=self.tail=new
        else:
            self.tail.next=new
            self.tail=new
            self.tail.next=self.head

    def display(self):
        temp=self.head
        if(temp==None):
            print("No elements are present")
        else:
            while(temp.next!=self.head):
                print(temp.data,end=" ")
                temp=temp.next
            print(self.tail.data,end="")
s=cll()
k=[int(a) for a in input("enter num:").split()]
for i in k:
    s.insertatbegin(i)
s.display()

