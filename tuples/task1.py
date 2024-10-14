n = int(input("Введите количество строк (n): "))
m = int(input("Введите количество символов в строке (m): "))

print(f"Введите {n} строк по {m} символов:")
d = [input() for _ in range(n)]

a = [ i for id, line in enumerate(d) for i, sym in enumerate(line) if sym == "*" ]
for id, line in enumerate(d):
    for i, j in enumerate(sorted(set(a))):
        line = list(line)
        line[j] = "*"
        d[id] = ''.join(line)
for id, line in enumerate(d): print(line)
