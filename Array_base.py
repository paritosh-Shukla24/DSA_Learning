##List
##It can have different datatypes in same list

l1=[]

l1.append(1)
l1.append(1.53)
l1.append("chicibib")
print(l1)

## Array is collection of elements stored in contiinous Memory Location.

##All Element of array are of  same data type 
##Properties
##->fixed size arr[5] ->homogenous nature(only float.only int)


## In python we use list as an array as hey provide more flexibility.
##Python provide ability to use array via libraries like numpy and array

# help()

import array

arr=array.array('i',[1,2,3,4,5])

print(arr)

arr[1]=10

print(arr)
