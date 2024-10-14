s = input("Введите уравнение вида 3-x=9: ")

def equation(eq):
    a, b, c= s[0], s[2], int(s[4])
    for i in [a, b]:
        if i.isdigit() and "-x" in s: d = -1 * int(i)
        elif i.isdigit(): d = int(i)
    if "-x" in s: return f"x = {-c - d}"
    elif "x" in s and f"-{d}" in s: return f"x = {c + d}"
    else: return f"x = {c - d}"
print(equation(s))
