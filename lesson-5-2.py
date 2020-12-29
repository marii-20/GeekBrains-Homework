#Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке


with open('lines_words.txt', 'r') as obj:
    content = obj.read()

    lines = True
    for line in content:
        lines += line.count('\n')

print(f'Содержимое файла:\n{content} \n')

print(f'Количество строк: {lines} \n')

with open('lines_words.txt', 'r') as obj:
    content = obj.read()
    content = content.split()

    for i in range(lines):
        print(f'Слов в {i + 1}-ой строке: {len(content[i])}')