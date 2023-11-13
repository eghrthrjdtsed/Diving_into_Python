char_ = {char: ord(char) for char in input('Введите текст: ').split()}
iter_ = iter(char_.items())
for _ in range(5):
    print(next(iter_))
