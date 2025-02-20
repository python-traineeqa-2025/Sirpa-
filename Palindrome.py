word=str(input("Enter a word:"))

reverse=word[::-1]

if str(word)==str(reverse):
    print("It is palindrome")
else:
    print("It is not palindrome")

print(word.upper())