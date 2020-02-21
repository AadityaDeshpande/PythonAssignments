import re

str1 = "Welcome to PSL."

str1 = "PSLsdfgsdg"

patternObj = re.compile("PSL")

print("PatternObj = ", patternObj)

matchObj = patternObj.match(str1) #match: check only beginning

searchObj = patternObj.search(str1) #search: check all String

print ("Match return: ",matchObj,"\nSearch return: ",searchObj)
