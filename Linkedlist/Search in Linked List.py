from common import createLLFromList,print_LL,Node

head = createLLFromList([1,2,3,4,5])

print_LL(head)

def search_by_value(head,value):
    temp = head
    index = 0


    while temp != None :
        if(temp.data == value):
            return index
        temp =temp.next
        index+=1

    return "Not Found"

def search_by_value_recursive(head,value,index=0):
    if head == None:
        return None
    if head.data==value:
        return index

    return search_by_value_recursive(head.next,value,index+1)














print("Searching ")
print(search_by_value_recursive(head,5))


        