#example of class oops

class car:
    def __init__(self,brand,color,model,price):
        self.brand=brand
        self.color=color
        self.model=model
        self.price=price
    
    def drive(self):
        print(f"The {self.color} {self.brand} {self.model} {self.price} is driving.🚗 ")

car1=car("Toyota","Red","Camry",30000)
car2=car("Honda","Blue","Civic",25000)
car3=car("Ford","Green","Mustang",40000)
car4=car("Chevrolet","Black","Malibu",28000)
car5=car("Nissan","White","Altima",27000)
car1.drive()
car2.drive()
car3.drive()
car4.drive()
car5.drive()