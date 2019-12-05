A = int(input())
B = int(input())
n = 1 
while not(((n - 1) % A == 0) and ((n + 1) % B == 0)):
    n = n + 1 
    print(n)
print(n)
