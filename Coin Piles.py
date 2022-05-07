n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    M = max(a,b)
    m = min(a,b)
    x = 2*m - M
    y = m/M if M != 0 else 1
    print("YES" if y == 0.5 or (x%3 == 0 and x >=0)  else "NO")


## print('YES' if (a+b) % 3 == 0 and a <= 2*b and b <= 2*a else 'NO')


# a = []
# for i in range(n):
#     a.append(input().split())   
#     a[i] = [int(x) for x in a[i]]
# for i in range(n):
#     M,m = max(a[i]),min(a[i])
#     x = 2*m - M
#     y = m/M if M != 0 else 1
#     print("YES" if y == 0.5 or (x%3 == 0 and x >=0)  else "NO") 