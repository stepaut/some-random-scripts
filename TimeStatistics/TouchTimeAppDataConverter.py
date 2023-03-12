import numpy as np
import pandas as pd
from datetime import datetime
import os

df = pd.read_csv('TimeStatistics/data/data.txt')
df['Start'] = pd.to_datetime(df['Start'])
df['End'] = pd.to_datetime(df['End'])
df = df.loc[:, ~df.columns.str.contains('^Unnamed')] # удалаяем битые столбцы
df['Total'] = df['Total'].str.extract('(\d+)').astype(int) # удаляем из Total 'min'

print(df.info())

activities = df.Activity.unique()

#first_year = df.Start.min().year
#last_year = df.End.max().year

#for year in range(first_year, last_year + 1):
year = 2023

weeks = range(1,54)
dfy = pd.DataFrame(0, index=np.arange(len(weeks)),columns=np.hstack(['week', activities]))
dfy['week'] = weeks

for index, row in df.iterrows():
    if (row.Start.year > year):
        continue
    if (row.Start.year < year):
        break
    
    dfy[row.Activity].iloc[row.Start.week - 1] += row.Total

dfy = dfy.loc[:, (dfy != 0).any(axis=0)] # удаляем столбцы, в которых все нули

os.makedirs('TimeStatistics/data', exist_ok=True) 
dfy.to_csv('TimeStatistics/data/' + str(year) + '.csv', index=False)