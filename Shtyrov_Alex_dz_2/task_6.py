"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""

import random


def recur(counter=10, answer=None):
    if counter == 10:
        print('В программе генерируется случайное целое число от 0 до 100. '
              'Отгадайте его за 10 попыток.')
        answer = random.randint(0, 100)
    if counter != 0:
        user_input = int(input('Ваш вариант ответа: '))
        if user_input == answer:
            print(f'Вы выиграли, правильный ответ {answer}.')
            raise SystemExit
        elif user_input < answer:
            print('Загаданное число больше.')
        elif user_input > answer:
            print('Загаданное число меньше.')
        return recur(counter - 1, answer)
    else:
        print('Вы проиграли.')


recur()
