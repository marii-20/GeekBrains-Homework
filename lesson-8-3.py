# Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка

class NotANumber(ValueError):
    def __init__(self, *args):
        self.my_list = []

my_list = []
while True:
    try:
        text = input('Введите число: ')
        if text == 'q':
            break
        if not text.isdigit():
            raise NotANumber(text)
        my_list.append(int(text))
    except NotANumber as e:
        print('Вы ввели неверный символ!')
print(my_list)