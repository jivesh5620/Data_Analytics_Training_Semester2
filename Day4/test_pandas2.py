import pandas as pd

data = [10,20,30,40,50,60,70,80,90,100]

series = pd.Series(data,index=['a','b','c','d','e','f','g','h','i','j'])
print(series)
print(series["i"])