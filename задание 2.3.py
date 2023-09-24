print("Введите число")

n = int(input())
a = 1
b = 1
c = ''
s = ''
j = n*len(str(n)) * 2 + len(str(n)) - 1

print(f"{repr(a).center(j)}")
print(f"{(repr(a) + repr(2) + repr(b)).center(j)}")

for i in range(3, n + 1):
    if len(str(i)) > 1 and len(str(i)) % 2 == 0:
        s = ''.join(reversed(str(i)))
        s = s[:len(str(i)) - 1]
        if i % 10 == 0:
            b = ''.join(reversed(c))
            if i == (n + 1):
                print(f"{(c + s + repr(i) + b).center(j)}")
            else:
                print(f"{(c + s + repr(i) + b).center(j)}")
        else:
            b = ''.join(reversed(c))
            if i == n + 1:
                print(f"{(c + s + repr(i) + b).center(j)}")
            else:
                print(f"{(c + s + repr(i) + b).center(j)}")
        c = c + repr(i)

    elif len(str(i)) > 1 and len(str(i)) % 2 != 0:
        s = ''.join(reversed(str(i)))
        s = s[:len(str(i))-1]
        if (i % 10) == 0:
            b = ''.join(reversed(c))
            if i == n + 1:
                print(f"{(c + s + repr(i) + b).center(j)}")
            else:
                print(f"{(c + s + repr(i) + b).center(j)}")
            c = c + repr(i)

        else:
            b = ''.join(reversed(c))
            if i == n + 1:
                print(f"{(c + s + repr(i) + b).center(j)}")
            else:
                print(f"{(c + s + repr(i) + b).center(j)}")
            c = c + repr(i)

    elif len(str(i)) == 1:
        a = a * 10 + (i - 1)
        d = (i - 1) * 10 ** (i - 2) + b
        b = d
        c = repr(a) + repr(i)
        if i == (n + 1):
            print(f"{repr(a) + repr(i) + repr(d)}")
        else:
            print(f"{(repr(a) + repr(i) + repr(d)).center(j)}")

