#Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.


number = input('Пожалуйста, введите целое положительное число: ')

i = 0
max = 0

while i != len(number):
    if int(number[i]) == 9:
        max = 9
        break
    if int(number[i]) > max:
        max = int(number[i])
    i += 1

print(f'В вашем числе {number}, {max} - самая большая цифра.')

