#Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента

from random import randint

numbers = [randint(1, 100) for i in range(10)]

new_l = [el for n, el in enumerate(numbers) if numbers[n - 1] < numbers[n]]


print(numbers)

print(new_l)


