# Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
# вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).Данные методы должны применяться только к
# клеткам и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно.
# В методе деления должно осуществляться округление значения до целого числа.

class Cell:
    def __init__(self, qty):
        self.qty = int(qty)

    def __str__(self):
        return f'{self.qty}'

    def __add__(self, other):
        return f'Полученный результат от сложения: {Cell(self.qty + other.qty)}'

    def __sub__(self, other):
         if self.qty - other.qty >= 0:
             return f'Полученный результат от вычитания: {self.qty - other.qty}'
         else:
             return 'Разность количества ячеек двух клеток меньше нуля!'

    def __mul__(self, other):
        return f'Полученный результат от умножения: {self.qty * other.qty}'

    def __truediv__(self, other):
        return f'Полученный результат от деления: {round(self.qty // other.qty)}'

    def make_order(self, line):
        l = ''
        for i in range(int(self.qty / line)):
            l += f'{"*" * line} \\n'
        l += f'{"*" * (self.qty % line)}'
        return l


set1 = Cell(33)
set2 = Cell(12)

print(set2)
print(set1 + set2)
print(set1 - set2)
print(set1 * set2)
print(set1 / set2)
print(set1.make_order(10))
