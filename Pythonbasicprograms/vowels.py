# count the vowels in a string given

word=str(input("Enter a word:"))
count=0

for i in word.upper():

    if i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
        count+=1

print("the number of vowels in the word are:",count)

