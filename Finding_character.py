ch = input("Enter a character: ")
if ch >= '0' and ch <= '9':
    print("Digit")
elif ch.isupper ():
    print("Uppercase character")
elif ch.islower ():
    print("Lowercase character")
else:
    print("Special character")

#output:
Enter a character: 6
Digit
