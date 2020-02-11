from random import randint
 
N = 10
a = []
for i in range(N):
    a.append(randint(1, 99))
print(a)
 
for j in range(N-1):
    for i in range(N-1-j):
        if a[i] < a[i+1]:
            tmp = a[i+1]
            a[i+1] = a[i]
            a[i] = tmp
print(a)
