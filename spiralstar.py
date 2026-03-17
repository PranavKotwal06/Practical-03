n = 7
a = [[" "]*n for _ in range(n)]

top, bottom, left, right = 0, n-1, 0, n-1

while top <= bottom and left <= right:
    for i in range(left, right+1):
        a[top][i] = "*"
    top += 1

    for i in range(top, bottom+1):
        a[i][right] = "*"
    right -= 1

    for i in range(right, left-1, -1):
        a[bottom][i] = "*"
    bottom -= 1

    for i in range(bottom, top-1, -1):
        a[i][left] = "*"
    left += 1

for row in a:
    print(" ".join(row))
