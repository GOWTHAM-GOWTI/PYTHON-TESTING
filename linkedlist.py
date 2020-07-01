class Node():
    def __init__(self,data=None):
        self.data=data
        self.next=None

    def __str__(self):
        return f"{self.data}"

class LinkedList():

    def __init__(self):
        self.head=None
        self.tail=None

    def add_val(self,x):

        if self.head==None:
            self.head= x
            self.tail=x
        else:
            self.tail.next=x
            self.tail=x



    def add_to_start(self,x):

        if self.head==None:
            self.head= x
            self.tail=x
        else:
            head=self.head
            self.head=x
            self.head.next=head


    def search_val(self,x):
        curr=self.head
        index=0
        while curr is not None:
            if curr.data==x:
                return f"{x} in index {index}"
            index += 1
            curr= curr.next
        else:
            return f"{x} Not found"

    def remoe_val(self,x):

        curr=self.head
        index=0
        while curr is not None:
            if index==x:
                curr.data=None
                print(mylinkedlist)
                return f"{x} removed"
            index += 1
            curr= curr.next
        else:
            return f"{x} not fount"

    def length(self):
        curr=self.head
        index=0
        while curr is not None:
            index += 1
            curr= curr.next
        return f"length is {index}"


    def __str__(self):
        to_print=""

        curr = self.head

        while curr is not None:
            to_print=to_print +  str(curr.data) + "->"
            curr= curr.next
        if to_print:
            return f"{to_print[:-2]} "
        else:
            return "[]"

    def reverse_list(self,current,previous):
        #[1->2->3->4->5->None]    [5->4->3->2->->1->None]\

        if self.head==None:
            return
        elif current.next==None:
            self.tail=self.head
            current.next=previous
            self.head=current
        else:
            next=current.next
            current.next=previous
            self.reverse_list(next,current)


nodes=Node(1)
node2=Node(2)
node3=Node(3)
node4=Node(4)
node5=Node(5)

#print(nodes)
mylinkedlist=LinkedList()
mylinkedlist.add_val(nodes)
mylinkedlist.add_val(node2)
mylinkedlist.add_val(node3)
mylinkedlist.add_val(node4)
mylinkedlist.add_val(node5)

print(mylinkedlist)
#mylinkedlist.add_to_start(nodes)
#mylinkedlist.add_to_start(node2)
#mylinkedlist.add_to_start(node3)
#mylinkedlist.add_to_start(node4)
print(mylinkedlist)
print(mylinkedlist.search_val(1))
print(mylinkedlist.remoe_val(2))
print(mylinkedlist.length())

mylinkedlist.reverse_list(mylinkedlist.head,None)
print(mylinkedlist)
#print(type(LinkedList))
