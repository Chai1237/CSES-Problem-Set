n = int(input())
o = n*(n+1)/2
l = [int(x) for x in input().split()]
print(int(o - sum(l)))