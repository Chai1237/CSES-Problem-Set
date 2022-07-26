def RH(x, y, r):
    for i in range(1, 9):
        n = [i, y]
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
    r = list(r)
    n = [x, y]
    if n not in r:
        return 0
    elif x == 8:
        return 1
    else:
        r = RH(x, y, r)
        if y == 1:
            r = RU(x, y, r)
        elif y == 8:
            r = RD(x, y, r)
        elif 1 < y and y < 8:
            r = RU(x, y, r)
            r = RD(x, y, r)
    return S(x+1, 1, r) + S(x+1, 2, r) + S(x+1, 3, r) + S(x+1, 4, r) + S(x+1, 5, r) + S(x+1, 6, r) + S(x+1, 7, r) + S(x+1, 8, r)

R, ans = [], 0
for x in range(1, 9):
    for y in range(1, 9):
        R.append([x, y])

for i in range(8,0,-1):
    row = list(input())
    if "*" in row:
        ind = row.index("*")+1
        R.remove([ind,i])
        for q in range(row.count("*")-1):
            ind = row.index("*",ind)+1
            R.remove([ind,i])

R = tuple(R)
for y in range(1, 9):
    ans += S(1, y, R)
print(ans)


# s = []
# chars = {".": 1, "*": 0}
# for i in range(8):
#     s.append(list(chars[x] for x in list(input())))
 
# queens = []
# count = 0
# l = 0
# def solve():
#     global count
#     global l
#     if l == 8:
#         count += 1
#     else:
#         for i in range(8):
#             if s[l][i] == 0 or i in queens:
#                 continue
#             if any(abs(l-x)==abs(i-y) for x,y in enumerate(queens)):
#                 continue
#             queens.append(i)
#             l += 1
#             solve()
#             l -= 1
#             queens.pop()
 
# solve()
# print(count)


# reserved = [[c == '*' for c in input()]for _ in range(8)]
 
# count = 0
# cols = [0] * 8
# diag1 = [0] *15
# diag2 = [0 ] * 15
 
# def queen(y):
 
#     global count,cols,diag1,diag2
 
#     if y == 8:
#         count += 1
#         return
 
#     for x in range(8):
#         if cols[x] or diag1[x +y] or diag2[x - y + 7] or reserved[y][x]:
#             continue
#         cols[x] = diag1[x + y] = diag2[x - y + 7] = 1
#         queen(y+1)
#         cols[x] = diag1[x + y] = diag2[x - y + 7] = 0
 
 
# queen(0)
# print(count)