""" Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый массив чисел,
соответствующих требованию. Элементы вывести в порядке их следования в исходном списке. Для выполнения задания
обязательно использовать генератор."""

from typing import Iterable, Callable
from itertools import filterfalse


def my_filter_false(func: Callable, iterable: Iterable) -> None:

    def default_func(x):

        return x

    func = default_func if func is None else func

    for i in iterable:
        if not func(i):
            yield i


if __name__ == '__main__':
    input_data = input('Пожалуйста введите целые числа разделяя их пробелами: ')

    try:
        source_list = tuple(map(int, input_data.split()))
    except ValueError:
        print('Неверно введенные данные')
        exit(1)


print(f'итоговый массив чисел {list(my_filter_false(lambda x: source_list.count(x) > 1, source_list))}')




