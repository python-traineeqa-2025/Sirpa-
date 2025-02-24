# get the fibonacci series after getting an input of the number
num=int(input("Enter a number:"))
a=0
c=1

print("The fibonacci series of the number is:",a,c,end=" ")

for i in range(2,num):
    f=a+c
    a=c
    c=f
    print(f,end=" ")
