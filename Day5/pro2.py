import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [7,21,30,40,55]

plt.figure(figsize=(4,3))
plt.plot(x, y,color='blue',marker = 'o',linestyle='--',linewidth =2,markersize = 12)

plt.title("St. Andrews Institute of Technology And Management")
plt.xlabel("My First Chart")
plt.ylabel("AIML - 2nd Semester")

plt.show()