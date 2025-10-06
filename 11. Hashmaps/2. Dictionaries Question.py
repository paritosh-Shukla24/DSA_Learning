
## 1. Intersection Of Two Arrays
def intersection_of_arrays(arr1, arr2):
    freq={}
    intersec=[]
    for num in arr1:
        freq[num]=freq.get(num,0)+1

    for num in arr2:
        if num in freq and freq[num]>0:
            intersec.append(num)
            freq[num]-=1
    return intersec

    pass

# Example Usage:
arr1 = [1, 2, 2, 1]
arr2 = [2, 2]
print(intersection_of_arrays(arr1, arr2))


# 2. Check for Duplicates

def contains_duplicates(nums):
    dict1={}
    for i in nums:
        dict1[i]=dict1.get(i,0)+1

    for key, value in dict1.items():
        if value>1:
            return True

    return False



# Example Usage:
nums1 = [1, 2, 3, 1]
nums2 = [1, 2, 3, 4]
print(contains_duplicates(nums1))  # Output: True
print(contains_duplicates(nums2))  # Output: False


# 3. First None Repeating Character in a string

def first_non_repeating_char(s):
    dict1={}
    for ch in s:
        dict1[ch]=dict1.get(ch,0)+1

    for key,value in dict1.items():
        if dict1[key]==1:
            break



    return key


    pass

# Example Usage:
s = "swiss"
print(first_non_repeating_char(s)) # 'w'


