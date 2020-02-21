'''
accept two digit number from keyboard, validate it to be exact two digit entry
'''
import re

str1 = input("Enter a 2 digit keywords")

pat = r"[0-9][0-9]"

matchObj = re.fullmatch(pat,str1)


print(matchObj)

if(matchObj != None):
    print("Found..!!!")

else:
    print("Not Found")
