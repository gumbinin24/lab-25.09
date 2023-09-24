print("Введите n")
n = int(input())
a = 1
b = 1
print(f'{repr(a).center(n*2)}')
print(f'{(repr(a) + repr(2) + repr(b)).center(n*2)}')
for i in range(3, n+1):
    a = a * 10 + (i-1)
    c = (i-1) * 10**(i-2) + b
    b = c
    if i == n + 1:
        print(f'{(repr(a) + repr(i) + repr(c))}')
    else:
        print(f'{(repr(a) + repr(i) + repr(c)).center(n*2)}')
 