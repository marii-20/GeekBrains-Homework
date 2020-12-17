#Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы
# с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после н

number = int(input('Введите число: '))
list = [9, 1, 5, 3, 4, 7, 7]
n = list.count(number)
for el in list:
    if n > 0:
        i = list.index(number)
        list.insert(i+n, number)
        break
    else:
        if number > el:
            l = list.index(el)
            list.insert(l, number)
            break
        elif number < list[len(list) - 1]:
            list.append(number)
print(list)