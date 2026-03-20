import pandas as pd

data = [5,10,15,20,25]
s = pd.Series(data)
print(s)

plus_five = s+5
print(plus_five)


multiply_two = s*2
print(multiply_two)

#printing the first three elements using a slice
print(s[0:3])