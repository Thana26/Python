def  has_duplicates(x):
    for i in x:
        if i not in res:
            res.append(i)
    print("list with out duplicates",res)
    return res
res = []
x = [1, 3, 5, 6,1]
print ("The original list is : " ,x)
print(has_duplicates(x))
