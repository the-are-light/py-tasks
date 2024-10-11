s = """..*.
.**."""
d = s.split("\n")
a = [ i for id, line in enumerate(d) for i, sym in enumerate(line) if sym == "*" ]
for id, line in enumerate(d):
    for i, j in enumerate(sorted(set(a))):
        line = list(line)
        line[j] = "*"
        d[id] = ''.join(line)
for id, line in enumerate(d): print(line)