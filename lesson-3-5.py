# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к
# полученной ранее сумме и после этого завершить программу

result = 0
total_sum = 0

while True:
    l = list(input('Введите числа через пробел: ').split())
    for el in range(len(l)):
        if el == '#':
            break
        else:
             result = result + int(l[el])
    total_sum = total_sum + result
    print(f'Сумма чисел: {result}')
print(f'Сумма всех чисел: {total_sum}')



