n = 5
a = [[0]*n for _ in range(n)]

num = 1
top, bottom, left, right = 0, n-1, 0, n-1

while top <= bottom and left <= right:
    for i in range(left, right+1):
        a[top][i] = num; num += 1
    top += 1

    for i in range(top, bottom+1):
        a[i][right] = num; num += 1
    right -= 1

    for i in range(right, left-1, -1):
        a[bottom][i] = num; num += 1
    bottom -= 1

    for i in range(bottom, top-1, -1):
        a[i][left] = num; num += 1
    left += 1

for row in a:
    print(*row)
