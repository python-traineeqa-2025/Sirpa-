i=list(map(int,input("Enter a list:").split()))

l2=[]
for a in i:
    if a%2==0:
        l2.append(a*a)

print('Square of even numbers:',l2)

# square rrot using function
def squr(num):
    return (num*num)

print(squr(4))
print()
