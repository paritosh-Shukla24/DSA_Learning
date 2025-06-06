arr=[10,101,21,41,2,16,37,98]

def selction(arr):
    n=len(arr)

    for i in range(0,n-1):
        m=i
        
        for j in range(i+1,n):
            if (arr[m]>arr[j]):
                m=j
        arr[i],arr[m]=arr[m],arr[i]
    
                 
    return arr

print(selction(arr))
