num=[int(x) for x in (input("Enter a list:").split())]

l2=[x+1 for x in num if x%2==0]
print(l2)


#
# for i in num:
#     if i%2==0:
#         i+=1
#         print(i)