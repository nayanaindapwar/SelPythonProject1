# Important Notes:
# Classes are user defined blue print or prototype
# We'll learn class variables, methods, instance variable, constructor etc
# Constructor is one method which is automatically called when you create object for any class.
# We need to call methods, constructor and variables outside of the class
# Two types of variables- class variables(defined inside the class) and instance variables (define inside the constructor)
# Class variables and instance variables have different purpose
# When we create an object that object is passed to the first argument in constructor and that is called as self.
# Self keyword is mandatory for calling variable names into method
# In python constructor name should be __init__()
# new keyword isn't required when you create the object

class Calculator:
    num = 100 # Class Variable

    # Default Constructor
    def __init__(self, a, b):
        self.firstNumber = a
        self.secondNumber = b
        print("I am called automatically when object of the class is created")

    def getData(self):
        print("I am now executing method in class")

    def addition(self):
        return self.firstNumber + self.secondNumber + Calculator.num
        # in above statement for num we can use Calculator.num or self.num, result is same for both


# obj = Calculator() - Syntax for Class object creation in python

obj = Calculator(2, 3)
obj.getData() # Calling the class method by using class object
print(obj.addition())

obj1 = Calculator(4, 5)
obj1.getData()
print(obj1.addition())





