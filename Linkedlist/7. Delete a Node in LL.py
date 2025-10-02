

from common import Node,take_input_better,print_LL

head = take_input_better()

print_LL(head)
def delete_at_head(head):
    if(head is None):
        return None
    head=head.next
    return head
print_LL(delete_at_head(head))

def is_tail_node(node):
    if(node==None):
        return True
    if(node.next == None):
        return True
    return False

def delete_at_tail(head):
    if(head is None):
        return None
    if head.next is None:
        return None
    head.next=delete_at_tail(head.next)
    return head
print_LL(delete_at_tail(head))

print_LL(head)
def delete_at_index(head,index):
    if(head is None):
        return None
    if index==0:

        return head.next
    head.next=delete_at_head(head.next,index-1)
    return head
print_LL(delete_at_index(head,0))



def delete_a_node_by_value(head,value):
    if(head is None):
        print("List Empty")
        return None
    
    if(head.data == value):
        return head.next # Boundary case when head is value
    
    temp = head

    while temp.next is not None and temp.next.data !=value:
        temp = temp.next

    if(temp.next is None):
        print("value not present")
        return head

    nodeToBeDeleted = temp.next
    nodeAfterDeletedNode = nodeToBeDeleted.next
    temp.next = nodeAfterDeletedNode

    return head



head = delete_a_node_by_value(head,3)
print("After Deletion")
print_LL(head)