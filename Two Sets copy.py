n, a,b = int(input()), [], []
n1 = [int(x) for x in input().split()]
n1.sort()
n1.reverse()
sa, sb = 0,0
for i in n1:
    if sa < sb:
        a.append(i)
        sa+=i
    else:
        b.append(i)
        sb+=i
if sa == sb:
    print(a, b)
else:
    print("NO SOLUTIOn")
