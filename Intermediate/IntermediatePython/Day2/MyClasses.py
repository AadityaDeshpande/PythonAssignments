"""
Rename to : Fucntional Programming
"""

list1 = [10,20,30,40,3]

squar_List1 = [i**2 for i in list1 ] #1) List Comprehension

print(squar_List1)

def makSqr(x):
    return x**2

mapObj = map(makSqr,list1) #2)using map with def function 

print(list(mapObj))

mapObj = map(lambda x: x**2,list1) #3) using map with Lambda

print(list(mapObj))

words = ["abc","xyz",345]

words2 = ["pqr","aadi","AADI",346]

mapObj = map(lambda word: word.upper() if type(word)==str else "" ,words)

#won't work as 2 parameters are expected
#mapObj = map(lambda word: word.upper() if type(word)==str else "" ,words,words2)

print(list(mapObj))

FilterObj = filter(lambda word: True if ( type(word)==str and word.islower() ) else False ,words)

print(list(FilterObj)) #Wont consider the Capitle Words


#FilterObj = filter(lambda x: x% 2 ==0,list1)

#print(list(FilterObj))
