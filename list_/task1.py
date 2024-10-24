

n = int(input("Введите количество городов: "))
roads = [list(map(int, input(f'Введите {n} дорог для города {i}: ').split())) for i in range(1, n+1)]
d = [[_, index] for _, i in enumerate(roads) for index, item in enumerate(i) if item == 1]
print(len(d)/2)
