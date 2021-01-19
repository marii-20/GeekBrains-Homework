# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники

class Warehouse:
    def __init__(self):
        self.dict = {}


    def add_item(self, equipment):
        self.dict.setdefault(equipment.group_name(), []).append(equipment)


    def remove_item(self, name):
        if self.dict[name]:
            self.dict.setdefault(name).pop(0)

class Equipment:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.group = self.__class__.__name__

        try:
            if year <= 1999:
                raise ValueError ('Устаревшая техника')
            else:
                print(year)

        except ValueError as e:
            print(e)

    def group_name(self):
        return f'{self.group}'

    def __repr__(self):
        return f'{self.name} - {self.year}'



class Printer(Equipment):
    def __init__(self, series, name, year):
        super().__init__(name, year)
        self.series = series

    def __repr__(self):
        return f'{self.name} - {self.series} - {self.year}'

    def action(self):
        return 'Печатает документы'


class Scanner(Equipment):
    def __init__(self, name, year):
        super().__init__(name, year)

    def action(self):
        return 'Сканирует документы'

class Xerox(Equipment):
    def __init__(self, name, year):
        super().__init__(name, year)

    def action(self):
        return 'Делает копии'



wh = Warehouse()

scanner = Scanner('hp', 2020)
wh.add_item(scanner)
scanner = Scanner('sony', 1998)
wh.add_item(scanner)
xerox = Xerox('xerox', 2003)
wh.add_item(xerox)
printer = Printer('mx-281', 'samsung', 2007)
wh.add_item(printer)

print(wh.dict)

wh.remove_item('Scanner')
print()
print(wh.dict)
