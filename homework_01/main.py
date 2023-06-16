"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """

    return list(map(lambda x: x ** 2, args))


# filter types
ODD = lambda x: x % 2 != 0
EVEN = lambda x: x % 2 == 0
PRIME = lambda x: x > 1 and all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))


def filter_numbers(lst, type_filter):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    return list(filter(type_filter, lst))
