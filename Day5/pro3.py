import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y1 = [10,20,30,40,50]
y2 = [20,30,35,45,55]

plt.plot(x,y1,label ='Sales 2024')
plt.plot(x,y2,label ='Sales 2025')

plt.title("YOY SALES")
plt.xlabel("Months")
plt.ylabel("Sales")

plt.legend()
plt.show()