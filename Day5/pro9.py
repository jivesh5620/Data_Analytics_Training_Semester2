import pandas as pd
import matplotlib.pyplot as plt
data = {
    'Month' : ['Jan','Feb','Mar','Apr'],
    'Sales' : [12000,11000,13000,25000]
}

df = pd.DataFrame(data)
print(df)

plt.bar(df['Month'], df['Sales'])
plt.title("Matplotlib with Pandas")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()