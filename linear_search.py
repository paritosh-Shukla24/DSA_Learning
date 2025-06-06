list1=[10,34,23,45,78,11]
target=780
def linear_search(list,tar):
    size=len(list)
    for i in range(size):
        if list[i]==tar:
            return i
        

    return -1


    
result=linear_search(list1,target)
print(result)