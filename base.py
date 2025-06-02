print("---------------------LIST OPERATIONS--------------------")
arr=[4,5,6,7,8]

arr.append(5)
print(arr)

arr.remove(4)
print(arr)

arr.insert(2,12)
print(arr)

arr.remove(8)
print(arr)

arr.sort()
print(arr)

##LIst Comprehension
print("---------------------LIST COMPREHENSION--------------------")

square=[x*x for x in range(10)]
print(square)

even=[x for x in range(20) if x%2==0]
print(even)
## for loop iteration
for val in arr:
    print(val)
##Important used in list,dictionary,string tuples
for i,val in enumerate(arr):
    print("Index",i,"Value",val)


## Useful Buil-ins in python

m=max(arr)
print(m)
m=min(arr)
print(m)
m=sorted(arr)
print(m)
m=sum(arr)
print(m)

a=[2,3,4]
b=[7,8,9]

zipped=list(zip(a,b))
print(zipped)


###SETS AND DICTIONARIES
print("---------------------SETS And Dictionaries--------------------")

s=set()
s.add(1)
print(s)
s.remove(1)
print(s)
d={'a':1,'b':2}

d['c']=3


for key,value in enumerate(d):
    print(key,value)


def factorial(n):
    if (n==0):
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))


## MAP and LAmbda filter iin Python
print("---------------------Lambda MAP and reduce filter--------------------")

nums=[1,2,3,4]

square=list(map(lambda x:x**2,nums))
## Lambda Creates a anonymous function like def square(x): and map iterates for each elements
print(square)

even=list(filter(lambda x:x%2==0,nums))
print(even)

from functools import reduce

total=reduce(lambda x,y:x+y,nums)

print(total)

print("---------------------String Tricks--------------------")

a="abdec"

print(a[::-1])
print(a.upper())
print(sorted(a))

print("".join(sorted(a)))

print(ord('a'))

print("---------------------Tuples Sorting--------------------")
zipped=[(2, 7), (3, 8), (4, 9)]
print(zipped.sort(key=lambda x: x[1]))


arr=list(map(int,input().split()))