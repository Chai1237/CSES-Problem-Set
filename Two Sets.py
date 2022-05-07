n = int(input())
a, b = [],[]
sa,sb = 0,0
n2 = n%100
t = (n2*(n2+1)/2)%10
if t%2 == 0:
    print("YES")
    for i in range(n, 0, -1):
        if (sa < sb):
            a.append(i)
            sa += i
        else:
            b.append(i)
            sb+= i

    l = [len(a), len(b)]
    a = ' '.join(map(str, a))
    b = ' '.join(map(str, b))
    print(l[0])
    print(a)
    print(l[1])
    print(b)
else:
    print("NO")