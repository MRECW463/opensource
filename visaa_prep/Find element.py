def search(arr,x):
    left,right=0, len(arr)-1
    while left<=right:
        mid=left+(right-left)
        if arr[mid]==x:
            return mid
        elif arr[mid]<x:
            left=mid+1
        else:
            right=mid-1
    return -1
n=int(input().strip())
arr=list(map(int,input().strip().split()))
x=int(input().strip())
result=search(arr,x)
print(result)
