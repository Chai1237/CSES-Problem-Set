n = int(input())
a = []
if n in [2,3]:
    print("NO SOLUTION")
else:
    for i in range(2,n+1,2):
        a.append(i)
    for i in range(1,n+1,2):
        a.append(i)
    for i in range(n):
        print(a[i], end =" ")


# n = int(input())
# if n in [2,3]:
#   print('NO SOLUTION')
# else:   
#   a = [str(i) for i in range()]
#   print (' '.join(a[1::2] + a[::2]))