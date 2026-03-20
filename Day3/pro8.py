import pandas as pd
a = {
    
    'Name' : ['Vansh','Diksha','Aman','Mohit','Dipankar','Jivesh','Ayush','Manas','Lakshay','Nishant','Abhinav','Harsh','Manik','Mayank','Sumit'],
    'Employee Id ' : [101565,102564,103575,104568,105688,106699,107698,108658,109885,110131,111446,112464,113476,114476,115466],
    'Age' : [25,18,19,20,10,19,56,47,79,25,66,46,36,25,64],
    'Salary' :[5000,8900,56744,46977,63479,99796,97979,46464,46466,88997,77979,79799,66979,464464,464464],
    

    
 }

data = pd.DataFrame(a)
print(data)
data.to_csv('data.csv')
