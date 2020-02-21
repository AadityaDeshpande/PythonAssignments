'''
OOP
'''

class SayHello:
    def __init__(self):
        print("IN Def")
        self.message = "HelloWorld..!!!"

    #@classmethod
    def display(self):
        print("inside display , self = ",self)
        self.message = "XYZ"
        
    

print("="*70)

#ob1 = SayHello("Hello")

ob1 = SayHello()

print(ob1.message)

ob1.display()

print(ob1.message)
#print(ob2)
