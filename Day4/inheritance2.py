#inheritance 2nd example
#inheritance definition: the process by which one class takes on the attributes and methods of another class
class Animal:
    def speak(self):
       print("Animal speaks")
class Dog(Animal):
    def speak(self):
        print("Woof!")
class Cat(Animal):
    def speak(self):
        print("Meow!")
class Bird(Animal):
    def speak(self):
        print("Chirp!")
    
for animal in (Dog(), Cat(), Bird()):
    animal.speak()    