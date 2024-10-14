
def lecture(s, n, m):
    return len(set(s[i:i + m] for i in range(n-m+1)))

n, m = map(int, input("Enter values n & m: ").split())
s = input("Enter the text of the lecture: ")

print(f"Количество слов длины {m}, которые профессор мог использовать в своей лекции:", lecture(s, n, m))
