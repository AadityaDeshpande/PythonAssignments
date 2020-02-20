class Employee:
    empCount = 0

    def __init__(self,name,sal):
        self.name = name
        self.sal = sal
        Employee.empCount += 1

    def display(self):
        print("name is ",self.name)
        print("sal is ",self.sal)

def main():
    emp1 = Employee("aadi",900000)
    emp2 = Employee("abcd",200000)
    emp1.display()
    emp2.display()


if __name__ == '__main__':
    main()
        
        
