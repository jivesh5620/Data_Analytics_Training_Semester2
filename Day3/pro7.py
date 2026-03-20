import pandas as pd
a = {
    'Name' : ['Vansh','Diksha','Aman','Mohit','Dipankar','Jivesh'],
    'Age' : [25,18,19,20,10,19],
    'Salary' :[5000,8900,56744,46977,63479,99796]

    
 }

df = pd.DataFrame(a)
print(df.shape)

df.rename(columns={'Salary' : 'Payement'},inplace = True)
print(df)
df.info()
df.describe()