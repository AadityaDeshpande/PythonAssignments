import re

str1 = "Welcome to PSL."

str1 = "PSLsdfgsdg"

#patternObj = re.compile("PSL")

#print("PatternObj = ", patternObj)

matchObj = re.match("PSL",str1) #match: check only beginning

searchObj = re.search("PSL",str1) #search: check all String

print ("Match return: ",matchObj,"\nSearch return: ",searchObj)


#use pre complied when need to check multiple time...
