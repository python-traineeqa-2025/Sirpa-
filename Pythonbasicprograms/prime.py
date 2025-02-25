p=int(input("Enter a number:"))

b=0
if p==1:
    print("It is not prime")
else:
    for i in range(1,p+1):
        if p%i==0:
            b+=1

    if b>2:
        print("it is not prime")
    else:
        print("it is prime")

