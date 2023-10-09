'''На вход подается словарь со списком вещей для похода в качестве ключа и их массой max_weight в качестве значения.

Определите какие вещи влезут в рюкзак backpack передав его максимальную грузоподъёмность.

Результат должен быть в виде словаря с вещами в рюкзаке:{предмет:вес}

*Верните все возможные варианты комплектации рюкзака.'''

items = {
    "ключи": 0.3,
    "кошелек": 0.2,
    "телефон": 0.5,
    "зажигалка": 0.1
}
max_weight = 1.0
from pprint import pprint

backpacks = []

for i in range(2 ** len(items)):
    backpack = {}
    weight = 0
    for j, item in enumerate(items):
        if i & (1 << j):
            if weight + items[item] <= max_weight:
                backpack[item] = items[item]
                weight += items[item]
            else:
                break
    backpacks.append(backpack)

result = [backpack for backpack in backpacks if backpack]

pprint(result)
