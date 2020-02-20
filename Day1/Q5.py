class Circle:
    pi = 3.14

    def __init__(self,radius):
        self.radius = radius

    
    def CalArea(self):
        return Circle.pi*self.radius*self.radius

    

def main():
    c1 = Circle(10)
    c2 = Circle(20)
    
    print("Area of circle 1 is = ",c1.CalArea())
    print("Area of circle 2 is = ",c2.CalArea())
    


if __name__ == '__main__':
    main()
        
        
