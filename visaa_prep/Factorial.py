def f(n):
    r=1
    for i in range(1,n+1):
        r*=i
    return r
n=int(input().strip())
print(f(n))
