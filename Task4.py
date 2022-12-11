# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k
# Пример:
# - k = 2 -> 2*x^2 + 4*x + 5 = 0 или x^2 + 5 = 0 или 10*x^2 = 0

from random import randint
k = int(input('Введите натуральную степень k: '))
a = randint(0, 100)
b = randint(0, 100)
print(f'{a}*x^{k} + {b}*x + 5 = 0')
with open('task_4.txt', 'w') as data:
    data.write(f'{a}*x^{k} + {b}*x + 5 = 0')