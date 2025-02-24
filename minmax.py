# Set a list and get the max,min numbers from it


l=[33,44,22,55,66,77]
greatest=l[0]
lowest=l[0]

for num in l:
        if(num>greatest):
            greatest=num
        elif(num<lowest):
            lowest=num

print("Greatest number:",greatest,"and lowest number:",lowest)


