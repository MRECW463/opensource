t=int(input().strip())
for _ in range(t):
    x,n=map(int,input().strip().split())
    a=x//10
    b=a*n
    print(b)
