# Создать (не программно) текстовый файл со следующим содержимым:One — 1 Two — 2 Three — 3 Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

dict = {}
rus_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_l = []

with open('one_two.txt', 'r', encoding="utf-8") as f_obj:
    for line in f_obj:
        k, v = line.split(' — ')
        dict[k] = v

rus_dict = {v:k for k, v in rus_dict.items()}
result = {i: dict[j] for i, j in rus_dict.items()}

print(result)

with open('one_two-2.txt', 'w', encoding="utf-8") as file_obj:
    file_obj.writelines(result)

