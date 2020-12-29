# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников

salary = {}
small_sal = {}

with open ('salary.txt', 'r', encoding="utf-8") as f_obj:
    content = f_obj.read()
    print(f'Список сотрудников: \n{content}')

with open('salary.txt', 'r', encoding="utf-8") as f_obj:
    for line in f_obj:
        key, value = line.split()
        salary[key] = int(value)
    for key, value in salary.items():
        if int(value) <= 20000:
            small_sal[key] = value
print(f'\nСотрудники с зарплатой до 20 тыс.: {small_sal}')

print(f'\nCредний оклад: {sum(map(int(salary[value]))) / len(salary)}')
