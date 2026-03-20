import pandas as pd

data = {"Math":90, "Science":85, "English":88}
series = pd.Series(data)
print(series)
print(series["Science"])