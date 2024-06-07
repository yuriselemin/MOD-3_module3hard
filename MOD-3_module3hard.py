

# Дополнительное практическое задание по модулю: "Подробнее о функциях."


def calculate_structure_sum(data_structure):
    # Если элемент является списком, применяем рекурсивный вызов функции
    if isinstance(data_structure, list):
        return sum(calculate_structure_sum(item) for item in data_structure)

    # Если элемент является словарем, суммируем значения, которые являются числами или строками
    elif isinstance(data_structure, dict):
        return sum(calculate_structure_sum(value) for value in data_structure.values() if isinstance(value, (int, str)))

    # Если элемент является кортежем, применяем рекурсивный вызов функции
    elif isinstance(data_structure, tuple):
        return sum(calculate_structure_sum(item) for item in data_structure)

    # Если элемент является строкой, возвращаем его как есть
    elif isinstance(data_structure, str):
        return data_structure

    # Если элемент не соответствует ни одному из вышеперечисленных типов, возвращаем 0
    else:
        return 0


# Пример использования функции
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)




