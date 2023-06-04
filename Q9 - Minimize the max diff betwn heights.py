k = list(map(int,input().strip().split()))
p = int(input())
k.sort()
n = len(k)
diff = k[n-1] - k[0]
mini = k[0] + p
maxi = k[n-1] - p 

for i in range (n-1):
    if k[i] < p :
        continue
    maxx = max(maxi,k[i] - p)
    minn = min(mini,k[i] + p)
    diff = min(diff,maxx - minn)
print(diff)


