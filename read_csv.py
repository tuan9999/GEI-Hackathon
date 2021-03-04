import pandas as pd
from functions import dropCol

file_path = "flint_test/test_data.csv"

df = pd.read_csv(file_path)
print(df.head())
print()
newdf = dropCol(df, ['Country'])
print(newdf.head())
