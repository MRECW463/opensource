n=int(input().strip())
a=1
for i in range(1,n+1):
    b=[]
    for j in range(i):
        b.append(str(a))
        a+=1
    print(" ".join(b))
