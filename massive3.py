from random import randint

N = 20
a = []
b = [] 
M = 1
tmp = 0
for i in range(N):
    a.append(randint(1, 100))
print(a)

for i in range(N-1):
    if a[i] < a[i+1]:
        M = M + 1
        tmp = M
    else:
        b.append(tmp)
        M = 0 
b.append(tmp)
K = len(b)
print(b)    

l = 0 
for i in range(K):
    if l < b[i]:
        l = b[i] 
print(l)
