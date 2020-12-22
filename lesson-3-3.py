#Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов

def my_func(a, b, c):
    if a < b and a < c:
        return int(b+c)
    elif b < a and b < c:
        return int(a+c)
    elif c < a and c < b:
        return int(b+a)

num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
num3 = int(input('Введите третье число: '))

result = my_func(num1, num2, num3)

print(f'Результат: {result}.')
