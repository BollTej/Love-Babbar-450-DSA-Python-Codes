k = list(map(int,input().strip().split()))
a = max(k)
b = int(0.5*(a**2 + a))
c = sum(k)
print(c-b)
