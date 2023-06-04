arr1 = list(map(int,input().strip().split()))
arr2 = list(map(int,input().strip().split()))
lst = []
print(list(set(arr1 + arr2)))
for i in arr1 :
    if i in arr2 :
        lst.append(i)
print(lst)


