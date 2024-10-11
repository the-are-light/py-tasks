def lecture(s, n, m):
    return len(set(s[i:i + m] for i in range(n-m+1)))

print(lecture("bbaabbbabb", 10, 3))
