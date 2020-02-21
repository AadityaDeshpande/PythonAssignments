

#OOPDemo9_special_method.py
class oPair:    # ordered pair
    def __init__(self, obj1, obj2):  # constructor
        self.data = (obj1, obj2)     # assign attribute

    def __str__(self):   	    # str() string representation
        return str(self.data) 	    # convert tuple to string
    __repr__ = __str__ 		    # repr() string representation

 
    def __add__(self, other):       # add two oPair objects, overriding of +
        return self.__class__(self.data[0] + other.data[0],self.data[1] + other.data[1])
class child(oPair):
    pass

#-------------------------------------------------
#myPair = oPair(6, -4) 	# create instance
#print ("myPair = ", myPair )  #calls str()
pair1 = child(6, -4)
pair2 = child(-5, 9)
print ("Pair 1= ",pair1)
print ("Pair 2= ",pair2)
pair3 = pair1 + pair2#pair1.__add__(pair2)
print ("Addition = ",pair3)    
print("isinstance(pair3,oPair) = ", isinstance(pair3,oPair))
print ("------------------------------------------------")

#print dir(oPair)

#print dir(object)


"""
def __add__(self, other):       # add two oPair objects
        return self.__class__(self.data[0] + other.data[0],self.data[1] + other.data[1])
    
"""
