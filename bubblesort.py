arr=[10,101,21,41,2,16,37,98]

def bubblesort_algo(arr):
    n=len(arr)
    for i in range(0,n-1):


        for j in range(0,n-i-1):
            if(arr[j]>arr[j+1]):
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp

    return arr
    
print(bubblesort_algo(arr))