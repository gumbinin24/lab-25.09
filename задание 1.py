print("Введите 3 числа")
a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print("3")
if ((a == b) and (c != (a and b))) or ((a == c) and (b != (a or c))) or ((c == b) and (a != (c or b))):
    print("2")
else:
    print("0")