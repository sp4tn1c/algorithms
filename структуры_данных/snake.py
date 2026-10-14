s = input().split()
n, m = int(s[0]), int(s[1])

answer = []
table = []
for i in range(n):
    table.append(input().split())

x = 0  
y = 0  

while x * 2 < n and y * 2 < m:
    
    if y * 2 < m:
        for i in range(y, m - y):
            answer.append(table[x][i])

    if x * 2 < n:
        for i in range(x + 1, n - x):
            answer.append(table[i][m - 1 - y])

    if x < n - 1 - x and y < m - 1 - y:
        for i in range(m - 2 - y, y - 1, -1):
            answer.append(table[n - 1 - x][i])
        
        for i in range(n - 2 - x, x, -1):
            answer.append(table[i][y])
    
    x += 1
    y += 1

print(' '.join(answer))
