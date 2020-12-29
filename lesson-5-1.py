# Создать программно файл в текстовом формате,
# записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

f = open('text.txt', 'tw', encoding="utf-8")

with open ('text.txt', 'w', encoding="utf-8") as f_obj:
    line = input('Введите слова или числа: ')
    while True:
        f_obj.writelines(line)
        if line == '':
            exit()

with open ('text.txt', 'r', encoding="utf-8") as f_obj:
    content = f_obj.read()
    print(content)

