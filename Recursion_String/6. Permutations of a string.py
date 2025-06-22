'''

Permutations of a string

'''

# def print_permutations(s1,takenSoFar):
#     if(len(s1)==0):
#         print(takenSoFar)
#         return
    
#     ourChar = s1[0]
#     smallInput = s1[1:]

#     for i in range(0,len(takenSoFar) +1):
#         print_permutations(smallInput, takenSoFar[0:i] + ourChar + takenSoFar[i:])

#     return
    
# print_permutations('abc','')



def permutations(s1,takenSoFar,lst):
    
    if len(s1)==0:
        print(takenSoFar)
        lst.append(takenSoFar)
        return lst
    
    ourchar=s1[0]
    smallinput=s1[1:]

    for i in range(0,len(takenSoFar)+1):
        permutations(smallinput,takenSoFar[0:i]+ourchar+takenSoFar[i:],lst)

    return lst
permutations('abc','',lst=[])

    


