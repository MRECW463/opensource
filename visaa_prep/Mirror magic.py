n=int(input())
a=[]
for _ in range(n):
    row=list(map(int,input().strip().split()))
    a.append(row)
mirror_image=[]
for row in a:
    mirror_image.append(row[::-1])
for row in mirror_image:
    print(' '.join(map(str,row)))
