import matplotlib.pyplot as plt

categoreies = ['Mon','Tue','Wed','Thu','Fri']
sales = [10,20,55,35,45]

y1 =[10,20,25,35,45]
y2 =[20,30,35,45,55]

plt.figure(figsize=(10,4))


plt.subplot(1,2,1)
plt.bar(categoreies,sales)
plt.title("Daily Sales")
plt.xlabel("Week Days")
plt.ylabel("Sales")

plt.subplot(1,2,2)
plt.scatter(y1,y2)
plt.title("User Example")
plt.xlabel("User1")
plt.ylabel("User2")

plt.show()