def nnod(n):
    if n>=1 and n<=9:
        return 1
    
    smallno=int(n/10)

    no=1+nnod(smallno)

    return no

print(nnod(10))