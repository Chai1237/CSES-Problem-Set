def S(n, a,b,c):
    if n == 1:
        return a + c
    return S(n-1, a, c, b) + a + c + S(n-1, b, a, c)
N = S(int(input()),"1","2","3")
print(len(N)//2)
for i in range(0,len(N),2):
    print(" ".join(N[i]+N[i+1]))