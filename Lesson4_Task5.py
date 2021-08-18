""" Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления
произведения всех элементов списка. Подсказка: использовать функцию reduce()."""


from functools import reduce


def my_func(el_p, el):
    return el_p * el


print(f'Список четных значений {[el for el in range(99, 1001) if el % 2 == 0]}')
print(f'Произведение чисел от 100 до 1000 включительно {reduce(my_func, [el for el in range(99, 1001) if el % 2 == 0])}')



# second solution for multiplication

from functools import reduce

result = reduce(lambda accum, i: accum * i, range(100, 1001))
print('Произведение чисел от 100 до 1000 включительно равно', result)

