# Instance Method
class Method:
    def __init__(self):  # Instance Method bcz self targeting to current object location
        pass


# Class Method
'''
    This method works with the class itself it will not target instance(object). We have to use @classmethod decorator for creating the class method and it takes cls as their first parameter.
'''

class MyClass:
    @classmethod  #decorator
    def class_method(cls):    #cls is instance location of MyClass
        print("This is class method")

'''
    Static Method: This method doesn't access class or instance directly it also uses a decorator @staticmethod it just act like a regular function placed in a class.
'''

class MyClass:
    @staticmethod
    def static_method():
        print("This is static method")