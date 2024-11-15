def rev(n):
    min=-2**31
    max=2**31-1
    a=-1 if n<0 else 1
    x=abs(n)
    m=int(str(x)[::-1])
    m*=a
    if m<min or m>max:
        return 0
    return m
n=int(input().strip())
result=rev(n)
print(result)
