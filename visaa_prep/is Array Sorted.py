def sorted(arr):
    for i in range(1,len(arr)):
        if arr[i]<arr[i-1]:
            return False
    return True
n=int(input())
arr=list(map(int,input().split()))
print("true" if sorted(arr) else "false")
