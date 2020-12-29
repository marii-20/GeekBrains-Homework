#Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков)

profit = {}
profit_1 = {}
proft = 0
average = 0
i = 0

with open('firm_income.txt', 'r', encoding="utf-8") as obj:
    for lines in obj:
        name, form, income, cost = lines.split()
        profit[name] = int(income) - int(cost)
        if profit.setdefault(name) >= 0:
            proft = proft + profit.setdefault(name)
            i += 1
    if i != 0:
        average = proft / i
        print(f'Средняя прибыль всех фирм: {average:.2f}')
    else:
        print(f'Убытки превышают прибыль. Фирмы работают в убыток')
    profit_1 = {'Средняя прибыль': round(average)}
    profit.update(profit_1)
    print(f'Прибыль для каждой фирмы: {profit}')

import json

with open('firm_income.json', 'w', encoding="utf-8") as f_obj:
    json.dump(profit, f_obj)
    prof_str = json.dumps(profit)