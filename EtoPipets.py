from random import randint
 
N = 15
a = []
b = [] 
M = 0 
P = 0
tmp = 0
for i in range(N):
    a.append(randint(1, 100))
print(a)

for i in range(N-1):
    b.append(tmp)
    if a[i] < a[i+1]:
        M = M + 1
        tmp = M
    else:
        b.append(tmp)
        M = 0 
for h in range(N-1):
    for i in range(N-1-h):
        if b[i] < b[i + 1]:
            P = b[i + 1]
            b[i + 1] = b[i]
            b[i] = 0
print(P+1)
