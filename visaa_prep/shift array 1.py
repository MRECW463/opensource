n=int(input())
arr=list(map(int,input().split()))
if n>1:
    a=arr[1:]+[arr[0]]
else:
    a=arr
print(" ".join(map(str,a)))
