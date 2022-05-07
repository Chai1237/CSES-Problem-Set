x, m, a, k = input(), [''], [], 0
t = list(set(x))
t.sort()
for i in t:
    k = x.count(i)/2
    if int(k) == k:
        a.append(i*int(k))
    else:
        m.append(i*int(k*2))
        if len(m) > 2:
            print("NO SOLUTION")
            quit()
print(''.join(a[:]+m[:]+a[::-1]))