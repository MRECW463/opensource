def c(n,m,arr):
    n1=0
    n2=0
    for nbr in arr:
        if nbr%m==0:
            n2+=nbr
        else:
            n1+=nbr
    return n2-n1
n,m=map(int,input().strip().split())
arr=list(map(int,input().strip().split()))
result=c(n,m,arr)
print(result)
