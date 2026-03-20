
import pandas as pd

data ={
    'Name' : ['jivesh', 'ajay', 'vijay'],
    'Age' : [21, 22, 23],
    'City' : ['Bangalore', 'Chennai', 'Pune'],
    'Marks' : [85, 90, 95]
}

df =pd.DataFrame(data)
print(df)
print(pd.__version__)