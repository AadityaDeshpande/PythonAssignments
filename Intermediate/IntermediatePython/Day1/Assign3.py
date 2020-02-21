'''
Accept a price value as:
	it shd begin with $ 
	should begin with at least one digit
	then decimal point .
	then exact 2 digit only
	
	e.g. $5.99 valid
'''
import re

str1 = input("Enter a String")

pat = r"\$\d+\.\d\d"

matchObj = re.fullmatch(pat,str1)

print(matchObj)

if(matchObj != None):
    print("Found..!!!")

else:
    print("Not Found")
