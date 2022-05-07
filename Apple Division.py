from itertools import combinations
n, a= int(input()), {}
e = [int(x) for x in input().split()]
s = sum(e)/2
for i in range(n//2,n):
    a[i] = list(combinations(e, i))
for i in range(n//2,n):
    for l in range(len(a[i])):
        e.append(sum(a[i][l]))
e = list(set(e))
e = list(map(lambda x: abs(x-s)*2, e))
print(int(min(e)))

# n = int(input())
# arr = [int(x) for x in input().split()]
 
 
# def solve(i,s1,s2):
#     if i == n:
#         return abs(s2-s1)
#     else:
#         return min(solve(i+1,s1+arr[i],s2),solve(i+1,s1,s2+arr[i]))
 
# print(solve(0,0,0))