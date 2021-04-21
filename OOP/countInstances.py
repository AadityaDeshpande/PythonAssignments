class Online:
    currently_online = []

    def __init__(self,data_use = 0):
        self.data_use = data_use
        Online.currently_online.append(self)

    def count_users(self):
        for i in Online.currently_online:
            print(i.data_use)
    
    @classmethod
    def count(cls):
        for i in cls.currently_online:
            print(i.data_use, "name =", i.__class__, "proper name = ", i.__class__.__name__)

    @staticmethod
    def isconnected():
        # code that does ping
        print(True)
        return True
    

# creating objects
me = Online(50)
me2 = Online(10)
mme3 = Online(5)

# invokes the classmethod
# implecitly sends the cls argument while calling.
Online.count()

# invokes objects method
# note 0 will be at end
Online().count_users()

# invokes the static method
# class related
Online.isconnected()

class Child(Online):
    pass

obj = Child()
obj.isconnected()


'''
D:\Scripts\python\PythonAssignments\OOP>python countInstances.py
50 name = <class '__main__.Online'> proper name =  Online
10 name = <class '__main__.Online'> proper name =  Online
5 name = <class '__main__.Online'> proper name =  Online
50
10
5
0
True
'''
