# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv


file_name, hours, per_hour, bonus, a = argv

print('Имя файла', file_name)
print('Выработка в часах: ', hours)
print('Стоимость ставки в час: ', per_hour)
print('Сумма премии: ', bonus)
print('Argv: ', a)

def wage (hours, per_hour, bonus):
    return (hours * per_hour) + bonus

total = wage(hours = int(hours), per_hour = int(per_hour), bonus = int(bonus))
print(f'Заработная плата сотрудника: {total}')