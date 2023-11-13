table = (
f'{k:2} * {j:2} = {j * k:2}' + (f'\n\n' if (k == 5 and j == 10) else f'\n' if k == 5 or k == 9 else f'\t')
    for i in range(0, 2) for j in range(2, 11) for k in range(2 + i * 4, 6 + i * 4)
)

print('ТАБЛИЦА УМНОЖЕНИЯ'.center(62))
[print(i, end='') for i in table]
