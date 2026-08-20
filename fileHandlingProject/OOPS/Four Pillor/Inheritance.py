'''
    In general terms Inheritance means property or any possession that comes to an heir.
    Property of parents class inherite by child class

    But out python neither have an old man or a chil then inheritance work where?

    It works between classes.

    Inheritance allows a class(child class) to inherit properties and behaviors(attributes and methods) from another class (parent class)

    Benefits of using inheritance is:

    Code reusability
    Organized structe
    Easy to maintain and extend

'''

class Factorymumbai: #parent class / superclass
    a = "I am an attribute mentioned inside Factory Mumbai"

    def hello(self):
        print("Hello I am a method mentioned inside FactoryMumbai")

class Factorypune(Factorymumbai): #child class / subclass
    pass

obj = Factorymumbai()

obj2 = Factorypune()
obj2.hello()

print(obj2.a)



###################################################################### 
# Constructor in Inheritance

class Animal:     #Single Inheritance
    def __init__(self, name: str):
        self.name = name
    def show(self):
        print(f"Hello your name is {self.name}")

class Human(Animal):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def show(self):
        print(f"Hello your name is {self.name} and age is {self.age}")

animal1 = Animal("Parwaz")
person1 = Human("Vineet",23)

animal1.show()
person1.show()

##Multiple Inheritance: There is two or more parent class and only one child class

class Animal:
    name1 = 'lion'
    def __init__(self,name):
        pass

class Human:
    name2 = 'Harsh'

    def __init__(self, name, age):
        pass

class Robot(Animal, Human):   #only ask name bcz of Animal, Human;
    name3 = "Jarvis"

obj = Robot() #want ask both name and age then create inheritance Human, Animal

print(obj.name1)
print(obj.name2)
print(obj.name3)
