def pal(s):
    return s==s[::-1]
s=input().strip()
if pal(s):
    print("TRUE")
else:
    print("FALSE")
