import re

str1 = input("Enter a valid Html tag : ")
pattern =r"^<(img)>[\w\s]+<\/\1>$"
if (re.search(pattern,str1)):
    print("Valid Pattern")
else:
    print("INVALID..!!")
