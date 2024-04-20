n = int(input("Enter Your Number : "))
for i in range(n):
    for l in range(i, n):
        print(" ", end = " ")
    for m in range(i+1):
        print(" * ", end = " ")
    print()
for i in range(n-1):
    for l in range(i+2 ):
        print(" ", end = " ")
    for m in range(i,n-1):
        print(" * ", end = " ")
    print()