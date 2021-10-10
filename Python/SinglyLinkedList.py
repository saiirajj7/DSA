#create a Node
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
#create a empty Linked List
class linkedList:
    def __init__(self):
        self.head=None
    def append(self, data):
        temp = Node(data)
        if self.head == None:
            self.head = temp
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = temp
    def display(self):
        curr = self.head
        while curr != None:
            print(curr.data)
            curr = curr.next
a_llist = linkedList()
n = int(input('How many elements would you like to add? '))
for i in range(n):
    data = int(input('Enter data item: '))
    a_llist.append(data)
a_llist.display()
# f_node = Node("Sai")
# l_list = LinkedList()
# l_list.append(f_node)
# s_node = Node("Raj")
# l_list.append(s_node)
# t_node = Node("Wah")
# l_list.append(t_node)
# l_list.display()