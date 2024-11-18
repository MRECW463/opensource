def update(n,m,grid):
    a=set()
    b=set()
    for i in range(n):
        for j in range(m):
            if grid[i][j]==0:
                a.add(i)
                b.add(j)
    for i in range(n):
        for j in range(m):
            if i in a or j in b:
                grid[i][j]=0
    return grid
n,m=map(int,input().split())
grid=[list(map(int,input().split())) for _ in range(n)]
final=update(n,m,grid)
for row in final:
    print(' '.join(map(str,row)))
