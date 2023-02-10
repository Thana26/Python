class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
    def Printing(self):
        if self.head==None:
            print("list is empty")
        else:
            temp=self.head
            while temp is not None:
                print("----->",temp.data,end="")
                temp=temp.next

    def ad_begin(self,data):
        new=Node(data)
        new.next=self.head
        self.head=new

    def ad_end(self,data):
        new=Node(data)
        temp=self.head
        while temp.next is None:
            temp.next=new
            new.next=None

    def afternode(self,data,pos):
        temp=self.head
        while temp.next is not None:
            if pos==temp.data:
                break
            else:
                temp=temp.next
        if temp is None:
            print("node is not present in linked list")
        else:
            new=Node(data)
            new.next=temp.next
            temp.next=new

    def befornode(self,data,pos):
        temp=self.head
        if self.head.data==pos:
            new=Node(data)
            new.next=self.head
            self.head=new
        else:
            while temp.next is not None:
                if temp.next.data==pos:
                    break
                temp=temp.next
        if temp.next is None:
            print("nide is nit present in the list")
        else:
            new=Node(data)
            new.next=temp.next
            temp.next=new

    def delatstart(self):
        self.head=self.head.next
        
    def delatend(self):
        #also write empty condition
        temp=self.head
        while temp.next.next is not None:
            temp=temp.next
        temp.next=None

    def delete(self,pos):
        #check for non
        temp=self.head
        if pos==self.head.data:
            self.head=self.head.next
        while temp.next is not None:
            if temp.next.data==pos:
                break
            temp=temp.next
        if temp.next is None:
            print("node is not present in the list")
        else:
            temp.next=temp.next.next



list1=SLL()
list1.ad_begin(10)
list1.ad_end(20)
list1.ad_begin(30)
list1.afternode(50,20)
list1.befornode(60,20)
# list1.delatstart()
# list1.delatend()
list1.Printing()
