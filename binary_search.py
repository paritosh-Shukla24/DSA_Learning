
sorted_list=[10,12,23,47,50,60,70]
target=60

def binary_search(list,target):
    lb=0
    ub=len(list)-1
    
    while(lb<=ub):
        mb=(lb+ub)//2
        if(list[mb]==target):
            return mb
        elif(list[mb]>target):
            ub=mb-1
        elif(list[mb]<target):
            lb=mb+1
    return -1

print(binary_search(sorted_list,target))