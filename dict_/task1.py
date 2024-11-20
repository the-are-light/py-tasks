n = int(input("Введите количество предприятий: "))
from collections import defaultdict
dict_ = defaultdict(list)
for i in range(n):
    item = input("Введите название предприятий, плановый объем розничного товарооборота, фактический объем розничного товарооборота через пробел: ").split()
    dict_[item[0]] = round(int(item[2])/int(item[1])*100, 2)

count = 0
for key, item in dict_.items():
    if item+10 < 100: count +=1
    print(f"Предприятие '{key}' выполнило план на {item}%")
print(f"\nКоличество предприятий, недовыполнивших план на 10% и более: {count}")
