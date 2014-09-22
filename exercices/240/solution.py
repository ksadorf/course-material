F = [1, 2, 3]
for i in range(3, 11):
        F.append(F[i - 1] + F[i - 2])
print(', '.join([str(u) for u in F]))
