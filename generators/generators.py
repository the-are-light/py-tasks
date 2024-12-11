def fib():
    a, b = 0, 1
    while b < 10000:
        yield b
        a, b = b, a+b
print(fib(), *[i for i in fib()])

def prime_nums(n):
    if n % 2 == 0: yield 2
    while n % 2 == 0: n//=2
    for i in range(3, int(n**0.5)+1, 2):
        while n % i == 0:
            yield i
            n //= i
    if n > 2: yield n

print(*[i for i in prime_nums(15)])

def degree(n, p):
    for i in range(0, p+1):
        yield n**i
print(degree(3, 4), *[i for i in degree(3, 4)] )


def prime_line(a, b):
    if b < 2: return None
    for num in range(a, b+1):
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                break
        else: yield num
print(*[i for i in prime_line(10, 1000)])
