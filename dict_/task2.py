n = int(input("Введите количество строк: "))
text=''
for i in range(n): text+=input()+'\n'
dict_ = {l: text.count(l) for id, line in enumerate(text.split("\n")) for i, l in enumerate(line.split()) if l!=""}
m = set(item for key, item in dict_.items())
from collections import defaultdict
dict_2 = defaultdict(list)
for key, item in dict_.items(): dict_2[item].append(key)
for i in list(set(dict_2))[::-1]: print(f"Частота: {i}\nСлова:", ", ".join(dict_2[i]))
