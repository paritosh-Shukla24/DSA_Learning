
# anslist=[]


def update_list(arr,x,indx):
    if (len(arr)==indx):
        return []
    
    anslist=update_list(arr,x,indx+1)
    if (arr[indx]==x):
        anslist.append(indx)
    
    

    return anslist

print(update_list([3,2,5,2,8,2,1],2,0))