t=int(input().strip())
for _ in range(t):
    n,m=map(int,input().strip().split())
    if n>m:
        a=n-m
    else:
        a=0
    print(a)
