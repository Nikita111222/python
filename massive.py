from random import randint 
N = 10
a = []
for k in range(N):
    a.append(randint(1, 100))
print(a)
for h in range(N-1):
    for i in range(N-1-h):
        if a[i] > a[i + 1]:
            tmp = a[i + 1]
            a[i + 1] = a[i]
            a[i] = tmp 
print(a)
