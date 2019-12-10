from random import randint 
a = []
for k in range(10):
    a.append(randint(1, 100))
print(a)
for h in range(9):
    for i in range(9-h):
        if a[i] > a[i + 1]:
            tmp = a[i + 1]
            a[i + 1] = a[i]
            a[i] = tmp 
print(a)
