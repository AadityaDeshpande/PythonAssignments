
#ignore case
'''

use a special meta character

^ for search at exactly at the beginning  r"^PSL"

$ for search at exactly at end            r"PSL$"

. for matching any single EXCEPT \n

(Search alternative patterns)

'''


import re

str1 = "Welcome to PSL. IBM in Pune. Wipro and Infosys"

pat1 = r"PSL|IBM|Infosys|Wipro" #Logical Seperation

searchObj = re.search(pat1,str1)

print ("Search return: ",searchObj)
