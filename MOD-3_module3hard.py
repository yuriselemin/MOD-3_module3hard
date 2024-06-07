

# Дополнительное практическое задание по модулю: "Подробнее о функциях."


def structure_sum(data):
    # Проверяем, является ли элемент числом или строкой
    if isinstance(data, int) or isinstance(data, float) or isinstance(data, str):
        return data
    # Если элемент - список или кортеж, применяем функцию к каждому элементу
    elif isinstance(data, list) or isinstance(data, tuple):
        return sum(structure_sum(x) for x in data)
    # Для словаря применяем функцию к значениям, если они числа
    elif isinstance(data, dict):
        return sum(structure_sum(value) for value in data.values() if isinstance(value, (int, float)))
    # Для кортежей с пустым списком и словарем применяем функцию к элементам
    elif data == ():
        return structure_sum(data[0])
    else:
        return structure_sum(data[0]) + structure_sum(data[1])

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = structure_sum(data_structure)
print(result)