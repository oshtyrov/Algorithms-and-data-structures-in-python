"""
2.	Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)
"""

# int (,16)
# reduce
# defaultdict

import collections
import functools

# Моё решение без collections

a = 'A2'
b = 'C4F'
sum_res = list((hex(int(a, 16) + int(b, 16)).upper())[2:])
prod_res = list((hex(int(a, 16) * int(b, 16)).upper())[2:])
print(sum_res)
print(prod_res)

# Решение из примеров в материалах. Разобрал, понял.


def calc():
    nums = collections.defaultdict(list)
    for d in range(2):
        n = input(f"Введите {d+1}-е натуральное шестнадцатиричное число: ")
        nums[f"{d+1}-{n}"] = list(n)

    summ = sum([int(''.join(i), 16) for i in nums.values()])
    # '%X'	Число в шестнадцатеричной системе счисления (буквы в верхнем регистре)
    print("Сумма: ", list('%X' % summ))

    mult = functools.reduce(lambda a, b: a * b, [int(''.join(i), 16) for i in nums.values()])
    print("Произведение: ", list('%X' % mult))


calc()
