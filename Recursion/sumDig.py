# def sOD(n):

#     if n>=1 and n<=9:
#         return n
    

#     small_no=int(n/10)
#     dig=int(n%10)
#     no=dig+sOD(small_no)

#     return no


# print(sOD(4675))


def pon(base,n):
    if n==0:
        return 1
    
    if n<0:
        return 1/pon(base,-n)
    
    half=pon(base,n//2)
    if n%2==0:
        return half*half
    
    else:
        return half * half * base
    
print(pon(2,3))
