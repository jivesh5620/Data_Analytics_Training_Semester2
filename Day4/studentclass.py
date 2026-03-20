#make a student record

class student:
    def __init__(self,name,age,rollno,branch):
        
        self.name = name
        self.age = age
        self.rollno = rollno
        self.branch = branch
        


    def record(self):
        print(".................Student Record Aviable..............")
        print(f"Name: {self.name} | Age: {self.age} | Roll no. {self.rollno} | Branch: {self.branch}")

record1 = student(input("Enter Your Name :"),input("Enter Your Age :"),input("Enter Your Roll No :"),input("Enter Your Branch :"))
record2 = student(input("Enter Your Name :"),input("Enter Your Age :"),input("Enter Your Roll No :"),input("Enter Your Branch :"))
record3 = student(input("Enter Your Name :"),input("Enter Your Age :"),input("Enter Your Roll No :"),input("Enter Your Branch :"))
record4 = student(input("Enter Your Name :"),input("Enter Your Age :"),input("Enter Your Roll No :"),input("Enter Your Branch :"))
record1.record()
record2.record()
record3.record()       
record4.record()       
