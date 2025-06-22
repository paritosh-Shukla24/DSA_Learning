def perm_list(s1):
    if s1=="":
        return [""]
    
    
    smallans=perm_list(s1[1:]) ##['bc','cb']
    mychar=s1[0]
    permututation=[]

    for eachterm in smallans:
        for i in range(0,len(eachterm)+1):
            permututation.append(eachterm[0:i]+mychar+eachterm[i:])

    return permututation

print(perm_list("abc"))

