

# Дополнительное практическое задание по модулю: "Подробнее о функциях."

def structure_sum(data):
    """
    Функция для вычисления суммы значений в структуре данных.
    Возвращает сумму числовых значений и длину строк. Для нашего списка данных рекурсивно применяет функцию
    к каждому элементу.
    """
    def sum_or_len(x):
        """
        Вспомогательная функция для определения типа элемента и его обработки.
        Возвращает значение элемента, если оно число или строка,
        иначе рекурсивно применяет функцию к каждому элементу списка или кортежа.
        """
        if isinstance(x, int) or isinstance(x, float):
            # Если элемент является числом, возвращаем его значение
            return x
        elif isinstance(x, str):
            # Если элемент является строкой, возвращаем её длину
            return len(x)
        else:
            # Если элемент является списком или кортежем, рекурсивно применяем функцию к каждому элементу
            return sum(sum_or_len(y) for y in x)

    # Возвращаем результат применения функции sum_or_len к входной структуре данных
    return sum_or_len(data)


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = structure_sum(data_structure)
print(result)