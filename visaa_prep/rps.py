r,p=input().split()
if r==p:
    print("NULL")
elif(r=='R' and p=='S') or\
    (r=='S' and p=='P') or\
    (r=='P' and p=='R'):
    print("Vignesh")
else:
    print("Charan")
