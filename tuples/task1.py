n = int(input("Введите количество строк (n): "))
m = int(input("Введите количество символов в строке (m): "))

print(f"Введите {n} строк по {m} символов:")
d = [input() for _ in range(n)]

x, y = [], []
for id, line in enumerate(d):
    for jid, jline in enumerate(line):
        if jline == "*":
            x.append(jid)
            y.append(id)

x, y = [min(x), max(x)], [min(y), max(y)]
print(f'Координаты: \nx ~ [{', '.join(map(str, x))}]\ny ~ [{', '.join(map(str, y))}]')

for id,line in enumerate(d):
    if id <= max(y) and id >= min(y):
        line = list(line)
        for j in range(x[0], x[1]+1): line[j] = "*"
        d[id] = ''.join(line)
    else: continue
        
for id, line in enumerate(d): print(line)
