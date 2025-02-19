a=int(input("Enter first number:"))
b=int(input("Enter Second number:"))

option=(int(input("add option:1, subtract: 2, multiply:3, divide:4")))

if option==1:
    sum=a+b
    print(sum)
elif option==2:
    diff=a-b
    print(diff)
elif option==3:
    mul=a*b
    print(mul)
else:
    div=a/b
    print(div)


