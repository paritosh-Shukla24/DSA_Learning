def sum_arr(lst):
    if len(lst)==0:
        return 0


    smallprob=sum_arr(lst[1:])



    return lst[0]+smallprob

print(sum_arr([1,2,3,4,5]))