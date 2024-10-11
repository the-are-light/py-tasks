
dict_ = {
    'Ромашка': [400, 370],
    'Василек': [600, 580],
    'Заря': [400, 280],
    'Малыш': [100000, 65000],
    'Сладкоежка': [2000000, 1400000],
    'Автолада': [500, 250]
}
from collections import defaultdict
dict_2 = defaultdict(list)
for key, item in dict_.items(): dict_2[key] = round(item[1]/item[0]*100, 2)
count = 0
for key, item in dict_2.items():
    if item+10 < 100: count+=1
for key, item in dict_2.items(): print(f"Предприятие '{key}' выполнило план на {item}%")
print(f"\nКоличество предприятий, недовыполнивших план на 10% и более: {count}")