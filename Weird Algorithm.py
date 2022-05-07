n = int(input())
a = [n]
while a[len(a)-1] != 1:
    if n%2 == 0:
        n//=2
        a.append(n)
    else:
        n = n*3+1
        a.append(n)
a = [str(x) for x in a]
print(' '.join(a[:]))