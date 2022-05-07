n = int(input())
a=[]
for i in range (n):
    a.append((input().split()))
    a[i]= [int(m) for m in a[i]] 
for i in range(n):
    y = max(a[i])
    x = min(a[i])
    if y == x:
        a[i] = 1+y*(y-2)+y
    else:
        if (max(a[i])%2 == 0 and a[i][0] > a[i][1]) or (max(a[i])%2 != 0 and a[i][0] < a[i][1]):
            a[i] = 1-x+y**2
        else:
            a[i] = 1 + y*(y-2)+x
for i in range(n):
    print(a[i])