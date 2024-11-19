def plane(x,n):
    a=x*100
    b=n-a
    c=(b+99)//100
    return c
x,n=map(int,input().split())
result=plane(x,n)
print(result)
