#inheritance example
class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def speak(self):
        print("Dog barks")

dog =Dog()
dog.speak()  # Output: Dog barks

