def gen(n):
    count = 0
    m = 2
    while count < n:
        for i in range(2, int(m ** 0.5) + 1):
            if m % i == 0:
                break
        else:
            count += 1
            yield m
        m += 1


print(*gen(20), sep='\n')
