from random import randint

N = 5
a = []
for i in range(N):
    a.append(randint(1,1000))
print(a)
    
nechet = 0
chet = 0
flag = 1
for i in range(N):
    if (a[i] % 2 == 0) and (chet < a[i]):
        chet = a[i]
        flag = 0
    if (a[i] % 2 == 1) and (nechet < a[i]):
        nechet = a[i]

if (flag == 0):
    print(chet)
else:
    print(nechet)
