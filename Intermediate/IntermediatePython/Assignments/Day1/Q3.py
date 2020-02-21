import re
    
def method1():

    words = ["abc", "123aaa", "xyz", "ABC" , "123", "ZZZZZ"]

    alpabetical_words =[ word for word in words if word.isalpha()]

    print(alpabetical_words)

def method2():
    words = ["abc", "123aaa", "xyz", "ABC" , "123", "ZZZZZ"]

    pat = r"^[a-zA-Z]+$"

    alpabetical_words =[ word for word in words if re.search(pat,word)]

    print(alpabetical_words)


    
    
if __name__ == '__main__':
    method1()
    method2()
    
