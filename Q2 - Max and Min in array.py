#for minimum element in array

k = list(map(int,input().strip().split()))
b = k[0]
for i in range (1,len(k)):
    b = min(b,k[i])
print(b)
#for maximum element in array

c = k[0]
for i in range (1,len(k)):
    c = max(c,k[i])
print(c)

