n,x,y=map(int,input().split())
a=n*x
if y<=a and y%x==0:
    print("YES")
else:
    print("NO")
