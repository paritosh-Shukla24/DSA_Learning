def check_sort(lst):
    if len(lst)==0 or len(lst)==1:
        return True
    
    # lst2=lst[1:]

    if lst[0]<lst[1]:
        return check_sort(lst[1:])
    
    else:
        return False
    

print(check_sort([1,2,5,3,4]))

l3 = [i for i in range(10000,1,-1) ]
# print(l3)
print(check_sort(l3))