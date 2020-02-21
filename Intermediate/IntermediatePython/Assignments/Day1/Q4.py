import re

str1 = input("Enter a String  ")

pat = r"^\$\d+\.\d{2}$"

if(re.search(pat,str1)):
    print("Valid")
else:
    print("Invalid")
