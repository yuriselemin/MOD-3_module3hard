

# Дополнительное практическое задание по модулю: "Подробнее о функциях."


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(list_):
    total_sum = 0  # Инициализация переменной для хранения суммы

    # Проверка типа элемента списка
    if isinstance(list_, (int, float)):
        return list_  # Если элемент является числом, возвращаем его значение
    elif isinstance(list_, str):
        return len(list_)  # Если элемент является строкой, возвращаем её длину
    elif isinstance(list_, (list, tuple, set)):
        for item in list_:  # Для каждого элемента вложенного списка/кортежа/множества
            total_sum += calculate_structure_sum(
                item)  # Вызываем функцию рекурсивно и добавляем результат к общей сумме
    elif isinstance(list_, dict):
        for key, value in list_.items():  # Для каждой пары ключ-значение в словаре
            total_sum += calculate_structure_sum(key) 
            total_sum += calculate_structure_sum(value) 
    return total_sum


result = calculate_structure_sum(data_structure)
print(result)





