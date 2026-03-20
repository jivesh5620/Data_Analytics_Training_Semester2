import matplotlib.pyplot as plt
import random

data =[random.randint(1,20) for _ in range(500)]
plt.hist(data, bins =20)
plt.title("Histogram Example")
plt.show()