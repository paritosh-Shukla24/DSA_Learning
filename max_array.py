def max_find(arr):
    first=-10000000000
    second=-10000000000

    for val in arr:
        if val>first:
            second=first
            first=val
            

        elif val>second and val!=first:
            second=val


    return first,second

arr=[6,10,3,3,9,100,1]
print(max_find(arr))