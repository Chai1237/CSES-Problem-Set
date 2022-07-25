N,s = 1,1
for i in range(int(input())):
    t = int(input())
    s = int(s)
    while N < t:
        s+=1
        N += len(str(s))
    s = str(s)
    print(s[-1] if N == t else s[-(N-t+1)])

