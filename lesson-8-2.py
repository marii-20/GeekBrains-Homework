# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать
# эту ситуацию и не завершиться с ошибкой

class DivisionByZero:
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    @staticmethod
    def division (num_1, num_2):
        try:
            return round((num_1 / num_2), 2)
        except:
            return f'Делить на ноль нельзя!'


nums = DivisionByZero(120, 5)
print(DivisionByZero.division(14, 2))
print(DivisionByZero.division(12, 0))
print(nums.division(64, 12))
print(nums.division(64, 0))