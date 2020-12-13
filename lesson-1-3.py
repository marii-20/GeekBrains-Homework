# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.


user_number = input('Пожалуйста, введите любое число: ')

number = int(user_number)
number_sum = int(user_number + user_number)
number_sum2 = int(user_number + user_number + user_number)

total = number + number_sum + number_sum2

print(total)