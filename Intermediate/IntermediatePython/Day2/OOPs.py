# parent class/super/base
class Parent:
    '''Parent class'''
    def __init__(self):
        print ('created an instance of', self.__class__.__name__ )  #pre defined attributes
# child class/sub/derived
class Child(Parent):                    # Child/sub/derived class inheriting from Parent/super/base
    pass
#--------------------------------------------------------------------------
# parent instance
p = Parent()
print ("class that got created=",p.__class__) #<class '__main__.Parent'>
print ("parent's parent class(es) if any = ",Parent.__bases__)#(<class 'object'>,)
print ("Parent doc string= ",Parent.__doc__) #Parent class
print ("Parent class atrributes = ",dir(Parent))
print ("-----------------------------------------------------")
# child instance
c = Child()
print ("child class that got created=",c.__class__)#<class '__main__.Child'>
print ("child's parent class(es) = ",Child.__bases__) # (<class '__main__.Parent'>,)
print ("child class attributes = ", dir(Child) )


