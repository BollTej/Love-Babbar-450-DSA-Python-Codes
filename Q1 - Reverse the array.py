k = list(map(int,input("Enter the array :").strip().split()))
print(k[::-1])

i = 0 
j = len(k) - 1 
while (j > i):
    k[i],k[j] = k[j],k[i]
    i += 1
    j -= 1
print(k)



