text = """
hi
hi
what is your name?
my name is bond
james bond
my name is damme
van damme
claude van damme
jean claude van damme
"""

dict_ = {l: text.count(l) for id, line in enumerate(text.split("\n")) for i, l in enumerate(line.split()) if l!=""}
m = set(item for key, item in dict_.items())
from collections import defaultdict
dict_2 = defaultdict(list)
for key, item in dict_.items(): dict_2[item].append(key)
for i in list(set(dict_2))[::-1]: print(f"Частота: {i}\nСлова:", ", ".join(dict_2[i]))