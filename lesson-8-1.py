# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число,
# месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Date():
    def __init__(self, date):
        self.date = date

    @classmethod
    def to_number(cls, date):
            user_date = []

            for i in date.split():
                if i != '-': user_date.append(i)
            return int(user_date[0]), int(user_date[1]), int(user_date[2])


    @staticmethod
    def valid(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if year <= 2021:
                    return f'Ok'
                else:
                    return f'Сейчас 2021 год.'
            else:
                return f'Такого месяца не существует.'
        else:
            return f'Такого дня не существует.'

    def __str__(self):
        return f'Текущая дата {Date.to_number(self.date)}'

today = Date('18 - 01 - 2008')
print(today)
print(Date.valid(16, 16, 2002))
print(today.valid(15, 11, 2023))
print(Date.to_number('02 - 07 - 2017'))
print(today.to_number('21 - 11 - 2020'))
print(Date.valid(36, 10, 2000))