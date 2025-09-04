
class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

def printLL(head):

    temp=head
    while temp is not None:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")

    temp = head
    while temp is not None:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")
    print("\nHead is still",head.data)



first = Node(1)
second = Node(2)
third = Node(3)

# print(id(first), id(second),id(third))

first.next = second
second.next = third




head = first

printLL(head)


#####

# Always avoid accessing any property on None

####
# print(third.next.data) # AttributeError: 'NoneType' object has no attribute 'data'


