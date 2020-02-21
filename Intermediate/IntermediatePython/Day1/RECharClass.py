'''
Search any 1 char class from a character class group mentioned

use a special meta character []

r"a|b|c|d" -----> [abcd]

[psl|wipro] ----> all OR ==>> p s l | w i p r o //any one character 

'''


import re

str1 = "Welcome to PSL. IBM in Pune. Wipro and Infosys"

pat1 = r"PSL|IBM|Infosys|Wipro" #Logical Seperation

searchObj = re.search(pat1,str1)

print ("Search return: ",searchObj)
