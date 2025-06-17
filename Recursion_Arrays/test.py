def indices_all(arr,element,idx=0):

    if (len(arr)==idx):
        return []
    
    if (arr[idx]==element):
        return [idx] + indices_all(arr,element,idx+1)
    else:
        return indices_all(arr,element,idx+1)

print(indices_all([3,2,5,2,8,2,1],2))