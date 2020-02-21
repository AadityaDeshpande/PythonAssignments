'''
OOP
'''

import copy

class SayHello:
    count = 0                   #class level variable--> Static variables
    
    def __init__(self,msg = "def Msg"):
        #print("IN Def")
        SayHello.count += 1 
        self.message = msg      #message is a instance property

    def copyConst(self,obj):
        self = obj
    
    #@classmethod
    def display(self):          #instance method
        print("inside display , self= ",self.message)
        self.message = "changed in display"

    @staticmethod               #no self parameter
    def getCount():
        return SayHello.count

def main():
    ob1 = SayHello("OB1")

    #ob1.display()
    
    ob2 = SayHello("OB2")

    #ob2.display()

    ob3 =SayHello("OB3")

    ob2.copyConst(ob3)

    ob1.display()
    
    ob2.display()

    ob3.display()

    print(SayHello.getCount())

    

if __name__=='__main__':
    main()
