gen = (i for i in range(0, 101, 2) if sum(int(j) for j in str(i))  != 8)
print(*gen)
