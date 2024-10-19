# Q1. Explain Class and Object with respect to Object-Oriented Programming. Give a suitable example.
# Answer-
'''Class - A class is a blue print for the object , To create object we require a model or plan or blueprint which is nothing but class. 
        It contains the properties(attributes) and action(behaviour) of the object
Object - An object is an Instance of a class ,The object is an entity that has a state and behaviour.In other words
         The physical existance of a class is nothing but an object.'''
# example
class person :
    
    def __init__(self , name , age , profession):
        self.name = name 
        self.age = age
        self.profession = profession 
    
    def show(self):
        print("Name :",self.name , "Age :",self.age ,"Profession :",self.profession)

# create object of a class         
p1 = person("Kartik", 21 , "Software developer")
p1.show()

# Q2. Name the four pillars of OOPs.
# Answer-
'''The four pillars of Object-Oriented Programming (OOPs) are:
    1. Polymorphism - The word "polymorphism" means "many forms" and in programming it refers to methods/function/operators with the same
                      name that can be executed on many objects or classes.
    2. Encapsulation - Encapsulation is the concept of building data and methods within a class and restricting access to some of the 
                       objects components to protect it's intigrity. 
    3. Inheritance - Inheritance allows us to define a class that inherits all the methods and properties from another class.
    
    4. Abstaction - An abstraction class can be considered a skelton or blueprint for other classes . '''
    
# Q3. Explain why the __init__() function is used. Give a suitable example.
# Answer-
'''The __init__() function in Python is a special method (also known as a constructor) that is automatically called when an object of a class
is created. It is used to initialize the attributes of the object with values when the object is instantiated.'''
# example
class book :
    
    def __init__ (self , title , author , pages):
        self.title = title
        self.author = author
        self.pages = pages
        
    def description (self):
        print("Title :",self.title ,"Author:",self.author,"Pages:",self.pages)
        
book1 = book("The Alchemist"," Paulo Coelho",208)
book1.description()

# Q4. Why self is used in OOPs?
# Answer-
'''self is used to represent the instance of the class within its methods. It allows the method to access and modify the attributes and 
methods of the instance.
It is used -
-To access instance variables
-Distinguish Between Class Attributes and Instance Attributes
-Allows Multiple Objects'''

# Q5. What is inheritance? Give an example for each type of inheritance.
# Answer- Inheritance
'''The process of inheriting the properties of the parent class into a child class is called inheritance. The existing class is called a
base class or parent class and the new class is called a subclass or child class or derived class.'''
# example
# 1.Single inheritance
class vehicle :
    def vehicle_info(self):
        print("this is my latest version of vehicle")
        
class car(vehicle):
    def car_info(self):
        print("this is my first car i have brought")
        
car = car()
car.vehicle_info()
car.car_info()

# 2.Multiple inheritance

class person :
    def person_info(self,name , age):
        print("inside person class")
        print("Name :",name , "Age:",age)
        
class company:
    def company_info(self , company_name, location):
        print("inside company class")
        print("Company Name:",company_name , "Location:",location )
        
class employee(person,company):
    def employee_info(self , salary , skill) :
        print("inside employee class")
        print("Salary:",salary,"Skill:",skill)

# create object of employee        
emp = employee()

emp.person_info("avil",23)
emp.company_info("Tesla","UK")
emp.employee_info(115000,"Allrounder")    


# 3.Multilevel inheritance


class vehicle :
    def vehicle_info(self):
        print("the latesh version to be upgraded")
        
class car(vehicle) :
    def car_info(self):
        print("include new features")

class bicycle(car) :
    def bicycle_info(self):
        print("include AI features")
        
# create object of bicycle
b_obj = bicycle()

b_obj.vehicle_info()
b_obj.car_info()
b_obj.bicycle_info()

# 4.Hierarchical Inheritance

class vehicle :
    def info(self):
        print("This is vehicle")
        
class car(vehicle) :
    def car_info(self , name):
        print("Car name is :", name)

class truck(vehicle):
    def truck_info(self,name):
        print("Truck name is :",name)
        
# create object of car 

obj1 = car()
obj1.info()
obj1.car_info("Rolls Royce")

# create object of truck 

obj2 = truck()
obj2.info()
obj2.truck_info("Mahindra ")
