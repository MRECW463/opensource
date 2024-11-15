n=int(input().strip())
k=int(input().strip())
b=1<<(k-1)
if n&b:
    print("true")
else:
    print("false")
