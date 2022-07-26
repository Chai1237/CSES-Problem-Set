def RHV(x, y, r):
    for i in range(1, 9):
        n = [i, y]
        if n in r:
            r.remove(n)
        n = [x, i]
        if n in r:
            r.remove(n)
    return r

def RU(x, y, r):
    for i in range(9 - x if x >= y else 9-y):
        n = [x, y]
        if n in r:
            r.remove(n)
        x += 1
        y += 1
    return r

def RD(x, y, r):
    for i in range(y if x+y <= 9 else 9-x):
        n = [x, y]
        if n in r:
            r.remove(n)
        x += 1
        y -= 1
    return r

def S(x, y, r):
    n = [x, y]
    if n not in r:
        return 0
    if x == 8:
        return 1
    else:
        r = RHV(x, y, r)
        if y == 1:
            r = RU(x, y, r)
        elif y == 8:
            r = RD(x, y, r)
        elif 1 < y and y < 8:
            r = RU(x, y, r)
            r = RD(x, y, r)
    return S(x+1, 1, r) + S(x+1, 2, r) + S(x+1, 3, r) + S(x+1, 4, r) + S(x+1, 5, r) + S(x+1, 6, r) + S(x+1, 7, r) + S(x+1, 8, r)

R, ans = [], 0

for y in range(1, 9):
    for x in range(1, 9):
        for y in range(1, 9):
            R.append([x, y])
    ans += S(1, y, R)

print(ans)
