# def anagram(str1,str2):

#     if len(str1)!=len(str2):
#         return False
    
#     dict1={}

#     for char in str1:
#         dict1[char]=dict1.get(char,0)+1
#     dict2={}
#     for char in str2:
#         dict2[char]=dict2.get(char,0)+1


#     return dict1==dict2

# print(anagram("om","mo"))

# def find_unique_char(s):
    

#     dict={}

#     for char in s:
#         dict[char]=dict.get(char,0)+1
#     print(dict)
#     for i,char in enumerate(dict):
#         print(i,char)

#     for i,char in enumerate(dict):
#         if dict[char]==1:
#             return i
        
     



#     return -1

# print(find_unique_char("Paritosh"))


# def annagrams(strs):

#     dict={}

#     for s in strs:
#         key=str(sorted(s))

#         if key not in dict:
#             dict[key]=[]

#         dict[key].append(s)


#     return [dict.values()]
# print(annagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

