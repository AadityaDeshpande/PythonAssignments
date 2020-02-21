class Circle:
    pi = 3.14
    all_Circles = []

    def __init__(self,radius):
        self.radius = radius
        Circle.all_Circles.append(self)


    def CalArea(self):
        return Circle.pi*self.radius*self.radius

    #generic static method is class method
    
    @classmethod
    def Total_Area(cls):
        total=0
        for c in cls.all_Circles:
            total = total+c.CalArea()
        return total

    

def main():
    c1 = Circle(10)
    c2 = Circle(20)
    
    print("Area of circle 1 is = ",c1.CalArea())
    print("Area of circle 2 is = ",c2.CalArea())
    print("Total Area is: ",Circle.Total_Area())

if __name__ == '__main__':
    main()
        
        
