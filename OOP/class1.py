class Person:
    name = 'Adam'
    surname = "hitler"

    def __repr__(self):
        return repr('Hello ' + self.name )

    # def __str__(self):
    #     return str(f"{self.name} is {self.surname}")

# repr is kind of backup if str is not there
p = Person()
print(p)

class MyStrings:
    name = "My name"
    # if comment below 2 line then <__main__.MyStrings object at 0x000001D7C3655E50>
    def __repr__(self):
        return "Mystring object"
    
    def __str__(self):
        return str(self.name)
st = MyStrings()
print(eval(repr(st)))

