sentence = 'It is raining cats and dogs'

token = sentence.split(" ")

print(token)

targetList = [ len(word) for word in token ]

print(targetList)
