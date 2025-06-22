# def palindrome_helper(s1,start,end):
 
#     if(start>=end):
#         return True
    
#     if(s1[start]!= s1[end]):
#         return False
    
#     return palindrome_helper(s1,start+1,end-1)
    

# def palindrome(s1):
#     return palindrome_helper(s1,0,len(s1)-1)



# print(palindrome('nitinr'))

def palindrom(str,start,end):
    if len(str)==0:
        return True
    if start>=end:
        return True
    if (str[start]!=str[end]):
        return False
    return palindrom(str,start+1,end-1)
s1='nitin'
print(palindrom(s1,start=0,end=len(s1)-1))