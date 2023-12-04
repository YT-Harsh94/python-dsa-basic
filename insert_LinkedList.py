class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def insert_begining(self,data):
         nb = node(data)
         nb.next = self.head
         self.head = nb   

    def display(self):
        if self.head is None:
            print("LinkedList is empty ")
        else:
            temp = self.head
            while temp:
                print(temp.data,"-->",end=" ")
                temp = temp.next

l = SingleLinkedList()
n1 = node(20)
l.head = n1
n2 = node(30)
n1.next = n2
n3 = node(40)
n2.next = n3

l.insert_begining(4)
l.display()                