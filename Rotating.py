n = 6
a = [[0]*n for _ in range(n)]

dirs = [(0,1),(1,0),(0,-1),(-1,0)]
d = 0

i = j = 0

for num in range(1, n*n + 1):
    a[i][j] = num
    
    ni = i + dirs[d][0]
    nj = j + dirs[d][1]
    
    if 0 <= ni < n and 0 <= nj < n and a[ni][nj] == 0:
        i, j = ni, nj
    else:
        d = (d + 1) % 4
        i += dirs[d][0]
        j += dirs[d][1]

for row in a:
    print(*row)
