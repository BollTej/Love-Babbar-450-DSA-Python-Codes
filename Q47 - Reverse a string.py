s = list(map(str,input().strip().split()))
a = 0
b = len(s)-1
while a <= b:
    s[a],s[b] = s[b],s[a]
    a += 1
    b -= 1
print(s)
