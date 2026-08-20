'''
Polymorphism is a core concept in Object - Oriented Programming(OOp). The word means "many forms: - and in programming.It allows the same interface
or method name to behave differently depending on the object or context.
'''

'''
    Types of Polymorphism
    - Polymorphism can be achieved in python in two ways well if we talk about compile time languages there are 3 ways but python does not support Method overloading.
    - Method overloading means having same name methods inside a class but parameters will be different but in python the latest definition will overwrite the previous one.
    -- Method Overriding
        - This is where a child class overrides a method of the parent class, and Python decides at runtime which method to call based on the object type.
        Example:- class Animal:
                    def saved(self):
                        print("Animal make a jungle save")

                class Human:
                    def saved(self):
                        print("Human save a animal")

                obj = Human()
                print(obj.saved)
    -- Duck Typing
	- Python follows the philosophy:
	"If it walks like a duck and quacks like a duck, it must be a duck."
	
	Example: 
		class Duck:
			def talk(self):
			print("Quack!")
			
		class Human:
			def talk(self):
			print("Hello!)
	- In the speak() function, we don't care if it's a Duck or a Human
		- We only care that the object has a talk() method.
'''