print("Введите n")
n = int(input())
for i in range(1, n+1):
    for g in range(1, i+1):
        print(g, sep = "", end = "")
    print()