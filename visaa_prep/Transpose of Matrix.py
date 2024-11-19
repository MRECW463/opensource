n=int(input())
a=[]
for _ in range(n):
    row=list(map(int,input().split()))
    a.append(row)
transpose=[[a[j][i] for j in range(n)] for i in range(n)]
for row in transpose:
    print(" ".join(map(str,row)))
