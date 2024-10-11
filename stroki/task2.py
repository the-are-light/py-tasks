

n, m = map(int, input().split())
lecture = input()
print(len(set(lecture[i:i + m] for i in range(n-m+1))))