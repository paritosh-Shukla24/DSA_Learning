"""

Searching Using Recursion

1. Linear Search
2. Binary Search

"""

def linear_rec(list,x,idx):
    if (len(list)==idx):
        return -1
    
    if (list[idx]==x):
        return idx
    
    return linear_rec(list,x,idx+1)

l1 = [i for i in range(15)]
print(l1)

print(linear_rec(l1,10,0))


    

# def LinearSearchUsingRecursion(l1,x,index):
#     # Base Case
#     if(len(l1) == index):
#         return False
    
    

#     ansFromRecursion = LinearSearchUsingRecursion(l1,x,index+1)

#     # if(ansFromRecursion == True):
#     #     return True
    
#     # if(l1[index]==x):
#     #     return True
#     # return False

#     return l1[index] == x or ansFromRecursion


# l1 = [i for i in range(100000)]
# ans = LinearSearchUsingRecursion(l1,10,0)

# print(ans)