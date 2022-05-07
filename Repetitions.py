dna = input()
n = 1
x = [1]
for i in range(len(dna)-1):
    x.append(1)
    if dna[i] == dna [i+1]:
        x[n]+=1
    else:
        n+=1
print (max(x))
