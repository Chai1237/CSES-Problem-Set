'''n = int(input())
a = [str(i) for i in range(1,n+1)]
print(' '.join(a[1::2] + a[::2]))'''
from collections import Counter
from time import time
from math import comb
from itertools import permutations, combinations
# files = open('PR input.txt','r')
start = time()

n = 0
def QP(x,y, A):
    A.append([x,y])
    H, a, b = [],[],[]
    if x != 8:
        return QP(x+1, 1, A) + QP(x+1, 2, A) + QP(x+1, 3, A) + QP(x+1, 4, A) + QP(x+1, 5, A) + QP(x+1, 6, A) + QP(x+1, 7, A) + QP(x+1, 8, A)
    else: 
        for i in range(8):
            n = A[i]
            print(len(A))
            H.append(n[1])
            a.append(n[0]+n[1])
            b.append(9-n[0]+n[1])
        H, a, b = set(H), set(a), set(b)
        if len(H) + len(a) + len(b) != 24:
            return 0
        else:
            return 1
for y in range(1,9):
    n += QP(1, y, [])

print(n)




# n, a= int(input()), {}
# e = [int(x) for x in input().split()]
# s = sum(e)/2
# for i in range(2,n):
#     a[i] = list(combinations(e, i))
# for i in range(2,n):
#     for l in range(len(a[i])):
#         e.append(sum(a[i][l]))
# e = list(set(e))
# e = list(map(lambda x: abs(x-s)*2, e))
# print(int(min(e)))
end = time()
print(end-start)

# n = int(input())
# if n in [2,3]:
#   print('NO SOLUTION')
# else:   
#   a = [str(i) for i in range()]
#   print (' '.join(a[1::2] + a[::2]))
#  func lambda x: x+5   == f(x) = x+5
#  map(lambda x: x+10, list)
# filter(lambda x: x%2 == 0, list) [output = even number in list]


#quit()
##LEARN
#Bitwise operator
# %s,>
#ord(string)

#if age >= 18 and not is_self_excluded:
#    print("You can gamble")
# if age >= 18 & ~is_self_excluded:
#    print("You can gamble")

# #Recursion
# def fact(x):
#     if(x == 0):
#         return 1
#     return n*fact(n-1)
# https://www.enjoyalgorithms.com/blog/recursion-explained-how-recursion-works-in-programming

