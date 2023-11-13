"""Создайте три (или более) отдельных классов животных. Например рыбы, птицы и т.п.
📌У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса.
📌Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.
📌Доработайте задачу 5.
📌Вынесите общие свойства и методы классов в класс Животное.
📌Остальные классы наследуйте от него.
Убедитесь, что в созданные ранее классы внесены правки."""


class Animals:
    def __init__(self, name, weight, color):
        self.name = name
        self.weight = weight
        self.color = color

    def info(self):
        print(f'Имя: {self.name}')


class Fish(Animals):
    def __init__(self, deepness, fin_num, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.deepness = deepness
        self.fin_num = fin_num
        if not self.name:
            self.name = 'Рыба'

    def info(self):
        super().info()
        print(f'У этой рыбы: {self.fin_num} плавников')


class Birds(Animals):
    def __init__(self, height, wingspan, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.height = height
        self.wingspan = wingspan

    def info(self):
        super().info()
        print(f'Размах крыльев: {self.wingspan}')


fish = Fish(5, 7, name='Окунь', weight=0.6, color='Gray')
print(fish.info())
