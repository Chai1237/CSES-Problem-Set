import math
def flr(x):
    return math.floor(x)
n = int(input())
z = 0
while flr(n/5) != 0:
    n = flr(n/5)
    z+=n
print(z)

'''n = int(input())
z = 0
while n >= 5:
    n //=5
    z+=n
print(z)'''