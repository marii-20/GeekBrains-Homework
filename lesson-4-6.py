# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.

# а):
from itertools import count

i = 0

for el in count(int(input('Введите число: '))):
    if i <= 30: # решила ограничить вывод элементов д 30 штук
        print(el)
    i += 1


# б):
i = 0

from itertools import cycle

l = ['hello', 13579, False, None, True]
for el in cycle(l):
    if i <= 30:
        print(el)
    i += 1