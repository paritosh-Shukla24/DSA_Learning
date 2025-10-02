from faiss import hashtable_int64_to_int64_add


class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

def print_LL(head):
    temp = head
    while(temp!=None):
        print(temp.data,end="->")
        temp = temp.next

    print()
    return
# return a head to a newly created LL
def take_input():
    value= int(input("Enter the value of the node"))
    head=None

    while(value!=-1):
        newNode=Node(value)

        if head==None:
            head=newNode

        else:
            temp=head
            while(temp.next!=None):
                temp=temp.next

            temp.next=newNode
        value = int(input("Enter the value of Node :- "))
    return head


















def take_input():
    value = int(input("Enter the value of Node :- "))
    head = None
    tail = None

    while(value != -1):
        newNode = Node(value)
        if(head == None):
            head = newNode
        else:
            temp = head
            while(temp.next!=None):
                temp=temp.next

            temp.next = newNode

        value = int(input("Enter the value of Node :- "))

    return head


def take_input_better():
    value = int(input("Enter the value of Node :- "))
    head = None
    tail = None
    
    while(value != -1):
        newNode = Node(value)
        if(head == None):
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
        
        value = int(input("Enter the value of Node :- "))
    
    return head




def input1():
    value=int(input("Enter the no"))
    head=None
    tail=None


    while(value!=-1):
        newNode = Node(value)
        if(head == None):
            head = newNode
            tail=newNode
        else:
            tail.next=newNode
            tail=newNode
        value=int(input("Enter the no"))

    return head

def insert(ele,head):
    ele=int(input("Enter the no"))
    insertNode = Node(ele)
    insertNode.next = head
    head=insertNode

    return head


def insert_at_end(ele,head):
    ele=int(input("Enter the no"))

    insertNode = Node(ele)
    temp=head
    while(temp!=None):
        temp=temp.next




newhead = input1()
insert_head = insert(6,newhead)
print_LL(insert_head)