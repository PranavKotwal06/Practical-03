n = 10
for i in range(3):
    for j in range(n):
        if (i + j) % 4 == 0:
            print("*", end="")
        elif (i == 1 and j % 4 == 0):
            print("*", end="")
        else:
            print(" ", end="")
    print()
