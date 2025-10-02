class Node:
    def __init__(self,value):
        self.data=value
        self.next = None


def printLL(head):
    temp=head
    while temp!=None:
        print(temp.data, end=" -> ")
        temp=temp.next

def printLength(head):
    temp=head
    count=0
    while temp!=None:
        count=count+1
        temp=temp.next
    return count




first=Node(8)
second = Node(9)
third = Node(10)
first.next=second
second.next=third
head=first
print(head.data)
print(head.next.data)
print(head.next.next.data)
print(printLL(head))
printLength(head)
print(printLength(head))