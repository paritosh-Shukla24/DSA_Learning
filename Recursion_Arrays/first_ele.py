def firstEle(lst,no):
    if len(lst)==0:
        return -1
    
    if (lst[0]==no):
        return 0
    
    ansFromRecursion=firstEle(lst[1:],no)
    
    if (ansFromRecursion==-1):
        return ansFromRecursion
    else:
        return ansFromRecursion+1

    # pass

def LastEle(lst,no):
    if len(lst)==0:
        return -1
    ansFromRecursion=firstEle(lst[:-1],no)
    if (lst[len(lst)-1]==no) and ansFromRecursion==-1:
        return len(lst) -1
    
    ansFromRecursion=firstEle(lst[:-1],no)
    
    # if (ansFromRecursion==-1):
    #     return ansFromRecursion
    # else:
    return ansFromRecursion
print(firstEle([4,5,3,5,6,7,7,55,8,4,5,9],11))

print(LastEle([4,5,3,5,6,7,7,55,8,4,5,9],8))