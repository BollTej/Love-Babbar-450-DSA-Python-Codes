#without using any sorting algorithm

k = list(map(int,input().strip().split()))
lst = []
a = k.count(0)
b = k.count(1)
c = k.count(2)
for i in range(a):
    lst.append(0)
for i in range(b):
    lst.append(1)
for i in range(c):
    lst.append(2)
print(lst)

#using dutch national flag algorithm 
k = list(map(int,input().strip().split()))
low,mid,high = 0,0,len(k) - 1
while mid <= high :
    if k[mid] == 0 :
        k[low],k[mid] = k[mid],k[low]
        low += 1
        mid += 1
    elif k[mid] == 1 :
        mid += 1
    elif k[mid] == 2 :
        k[mid], k[high] = k[high], k[mid]
        high -= 1
print(k)



