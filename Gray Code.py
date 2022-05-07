n, a, v = int(input()), [], ''
l = [int(x) for x in range(n)]
for i in range(2**n):
    v = str(bin((i^(i>>1))))
    a.append(v)
for i in range(2**n):
    print(a[i][2:].rjust(n,'0'))
