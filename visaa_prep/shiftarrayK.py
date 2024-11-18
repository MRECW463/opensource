def rotate(n,K,arr):
    K=K%n
    def array(sub_arr,start,end):
        while start<end:
            sub_arr[start],sub_arr[end]=sub_arr[end],sub_arr[start]
            start+=1
            end-=1
    array(arr,0,n-1)
    array(arr,0,K-1)
    array(arr,K,n-1)
    return arr
n=int(input())
arr=list(map(int,input().split()))
K=int(input())
rotated=rotate(n,K,arr)
print(' '.join(map(str,rotated)))
