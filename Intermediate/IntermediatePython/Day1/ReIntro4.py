
#ignore case
'''

use a special meta character

^ for search at exactly at the beginning  r"^PSL"

$ for search at exactly at end            r"PSL$"

. for matching any single EXCEPT \n

'''


import re

str1 = "Welcome to PSL."

str1 = "PSLsdfgsdg"

pat1 = r"^PSL"

pat2 = r"PSL$"

#patternObj = re.compile("PSL")

#print("PatternObj = ", patternObj)

matchObj = re.match(pat1,str1) #match: check only beginning

searchObj = re.search(pat2,str1) #search: check all String

print ("Match return: ",matchObj.group(),"\nSearch return: ",searchObj)


#use pre complied when need to check multiple time...
