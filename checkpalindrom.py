var = input("Enter your string:")
rev_var = ""

for i in var:
    rev_var = i + rev_var

if rev_var == var :
    print("Palindrome")
else:
    print("Not palindrome")
    

