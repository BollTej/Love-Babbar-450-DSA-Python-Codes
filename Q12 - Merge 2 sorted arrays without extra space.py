p = list(map(int,input().strip().split()))
q = list(map(int,input().strip().split()))
i1 = len(p) - 1
i2 = 0 
while i1 >= 0 and i2 < len(q) :
    if q[i2] < p[i1] :
        q[i2],p[i1] = p[i1],q[i2]
        i1 -= 1
        i2 += 1
    else :
        break 
p.sort()
q.sort()
print(p)
print(q)
print(p+q)

#second method
arr = p + q
arr.sort()
print(arr)