n, m = map(int, input("Enter values n & m: ").split())

list_ = [i*j for j in range(1, m+1) for i in range(1, n+1)]
red = [item for i, item in enumerate(list_) if item % 2 == 0 and (item % 3 != 0 and item % 5 != 0)]
green = [item for i, item in enumerate(list_) if item % 3 == 0 and item % 5 != 0]
blue = [item for i, item in enumerate(list_) if item % 5 == 0]
black = [item for i, item in enumerate(list_) if item % 2 != 0 and item % 3 != 0 and item % 5 != 0]
print(f"RED: {len(red)}\nGREEN: {len(green)}\nBLUE: {len(blue)}\nBLACK: {len(black)}")