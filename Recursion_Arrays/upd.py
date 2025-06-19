def update_list(arr,x,indx,anslist):
    if (len(arr)==indx):
        return 
    
    update_list(arr,x,indx+1,anslist)
    if (arr[indx]==x):
        anslist.append(indx)
    
    

    return anslist
ansList=[]
print(update_list([3,2,5,2,8,2,1],8,0,ansList))