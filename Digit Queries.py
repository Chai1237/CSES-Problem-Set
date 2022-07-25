for i in range(int(input())):
    t, Sum, SumL, n = int(input()), 0, 0, 0
    while Sum < t:
        n += 1 
        SumL = Sum
        Sum += 9*n*(10**(n-1))
    T = (t-SumL)//n
    p = t-SumL-(n*T)-1
    if n == 1:
        print(t)
    elif p < 0 :
        print(str(T-1)[p])
    else:
        A = 10**(n-1)+T
        print(str(A)[p])

# N,s = 1,1
# for i in range(int(input())):
#     t = int(input())
#     s = int(s)
#     while N < t:
#         s+=1
#         N += len(str(s))
#     s = str(s)
#     print(s[-1] if N == t else s[-(N-t+1)])

# q = int(input())
 
# def get_digit(index):
#     """Get the index-th digit of the fractional part.
#     """
#     i = 1
#     n = 9
#     while index - n * i > 0:
#         index -= n * i
#         i += 1
#         n *= 10
#     the_number = 10 ** (i-1) + (index-1) // i
#     return int(str(the_number)[(index%i)-1])
 
# for _ in range(q):
#     print(get_digit(int(input())))