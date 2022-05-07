from itertools import permutations
n = [str(x) for x in input()]
a = sorted(list(set(permutations(n))))
print(len(a))
for i in range(len(a)):
    print(''.join(a[i][:]))