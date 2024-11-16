a=int(input().strip())
if a<1 or a>12:
    print("Invalid")
elif a>=3 and a<=5:
    print("Spring")
elif a>=6 and a<=8:
    print("Summer")
elif a>=9 and a<=11:
    print("Autumn")
else:
    print("Winter")
