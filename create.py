class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SingleLinkedList: 
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("List is Empty")
        else:
            temp = self.head
            while temp:
                print(temp.data,"-->",end=" ")
                temp = temp.next

L = SingleLinkedList()
n = node(10)
L.head = n
n1 = node(20)
L.head.next = n1
n2 = node(30)
n1.next = n2
L.display()
                