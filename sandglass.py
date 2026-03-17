n = 5

# upper
for i in range(n, 0, -1):
    print(" " * (n - i) + "* " * i)

# lower
for i in range(2, n + 1):
    print(" " * (n - i) + "* " * i)
