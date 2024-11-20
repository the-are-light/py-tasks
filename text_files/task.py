file = input("Введите название .txt файла: ")

text = open(f"{file}.txt", mode='r', encoding='utf-8').read()
d = text.strip().split("textLines:")

roles = d[0].replace("roles:", '').strip().split("\n")
textLines = d[1].strip().split("\n")
result = []

for item in textLines:
        # Извлекаем роль из строки
        role = item.split(":")[0].strip()
        if any(role in jitem.strip() for jitem in roles):
            result.append(item)
        else:
            if result: result[-1] += "\n" + item

from collections import defaultdict
dict_ = defaultdict(list)
for i, item in enumerate(roles):
    for j, jitem in enumerate(result):
        if jitem.split(":")[0].strip() in item:
            dict_[item].append([j, " ".join(jitem.split(":")[1:])])

for i, item in enumerate(roles):
    if dict_[item]: pass
    else: dict_[item].append("нет слов")

for key, item in dict_.items():
    s = ''
    if item[0] == 'нет слов': print(f"{key}: {item[0]}")
    else:
        for i, jitem in item: s+=f"{int(i)+1}) {jitem}\n"

        print(f"{key}:\n{s}")
