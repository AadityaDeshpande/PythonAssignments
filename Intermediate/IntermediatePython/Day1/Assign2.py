'''
accept a word from keyboard validate only alphabetical content
'''
import re

str1 = input("Enter a Alphabet")

pat = r"[a-zA-Z]+"

matchObj = re.fullmatch(pat,str1)


print(matchObj)

if(matchObj != None):
    print("Found..!!!")

else:
    print("Not Found")
