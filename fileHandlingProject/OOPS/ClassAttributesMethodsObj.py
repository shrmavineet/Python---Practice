class Factory:
    age = 24     #attributes

    def printfunction(self, name:str): #self use as a location for an object
        print(f"Your name is {name} and age is {24}")

    def Method(self):   #Method
        print("Hello World!")

obj = Factory()  #Object

obj.printfunction("Vineet")

obj.Method()

