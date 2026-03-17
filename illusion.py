n = 5

for i in range(n):
    print(" "*(n-i), end="")
    print("*"*n)

for i in range(n):
    print("*"*n + " "*i + "*")

for i in range(n):
    print("*"*(n+1))
