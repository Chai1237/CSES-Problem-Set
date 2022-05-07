n = int(input())
a = [int(x) for x in input().split(' ')]
steps = 0
for i in range(1,n):
    if a[i-1] > a[i]:
        steps += (a[i-1]-a[i])
        a[i] = a[i-1]
print(steps)