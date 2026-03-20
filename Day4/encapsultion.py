#encapsulation example
#encapsulation defintion: restricting direct access to some of an object's components

class Person:
    def __init__(self,name,age):
        self.name = name #public attribute
        self.__age = age #private attribute


p1 = Person("John",30)
print(p1.name) #accessing public attribute
print(p1.__age) #trying to access private attribute will raise an error