a, b, c, *d = input('Введите строку из 4 и более целых чисел разделенных символом "/": ').split('/')
dict_ = {int(b): int(a), int(c): tuple(map(int, d))}
print(dict_)